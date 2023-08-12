from models import UsuarioModel
from utilitarios import conexion
from flask_restful import Resource, request
from dtos import UsuarioRequestDto, UsuarioResponseDto, LoginRequestDto, CambiarPasswordRequestDto
from bcrypt import gensalt, hashpw, checkpw
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from mensajeria import CambiarPassword

class RegistroController(Resource):
    def post(self):
        """
        file: registroUsuarioSwagger.yml
        """
        try:
            dto=UsuarioRequestDto()
            dataValidada = dto.load(request.get_json())


            salt = gensalt()

            password = dataValidada.get('password')
            passwordBytes = bytes(password, 'utf-8')

            passwordHaseada = hashpw(passwordBytes, salt).decode('utf-8')

            dataValidada['password'] = passwordHaseada

            nuevoUsuario = UsuarioModel(**dataValidada)

            conexion.session.add(nuevoUsuario)
            conexion.session.commit()

            dtoResponse = UsuarioResponseDto()

            return {
                'message': 'Usuario creado exitosamente',
                'content': dtoResponse.dump(nuevoUsuario)
            }

        except Exception as e:
            return {
                'message': 'Error al crear el usuario',
                'content': e.args
            }, 400
        
class LoginController(Resource):
    def post(self):
        """
        file: loginSwagger.yml
        """
        dto = LoginRequestDto()
        try:
            dataValidada = dto.load(request.get_json())
            usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(correo = dataValidada.get('correo')).first()

            if not usuarioEncontrado:
                return {
                    'message': 'El usuario no existe'
                }, 400
            
            password = bytes(usuarioEncontrado.password, 'utf-8')
            passwordEntrante = bytes(dataValidada.get('password'), 'utf-8')
            
            resultado = checkpw(passwordEntrante, password)

            if resultado == False:
                return {
                    'message': 'Credenciales incorrectas'
                }, 400
            
            token = create_access_token(identity=usuarioEncontrado.id)
            print(token)
            return{
                'content': token
            }

        except Exception as e:
            return {
                'message': 'Error al hacer el login',
                'content': e.args
            }, 400
        
class UsuarioController(Resource):
    @jwt_required()
    def get(self):
        identity = get_jwt_identity()

        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by( id = identity ).first()

        if not usuarioEncontrado:
            return{
                'message': 'El usuario no existe'
            }, 404
        
        dto = UsuarioResponseDto()

        return {
            'content': dto.dump(usuarioEncontrado)
        }

class CambiarPasswordController(Resource):

    @jwt_required()
    def post(self):
        data = request.get_json()
        dto = CambiarPasswordRequestDto()
        identity = get_jwt_identity()
        try:
            dataValidada = dto.load(data)
            usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id = identity).first()

            if not usuarioEncontrado:
                return {
                    'message': 'El usuario no existe'
                },404
            password = bytes(dataValidada.get('password'), 'utf-8')
            hashedPassword = bytes(usuarioEncontrado.password, 'utf-8')
            if checkpw(password, hashedPassword) == False:
                return {
                    'message': 'No es la contraseña'
                }, 400
            
            nuevaPassword = bytes(dataValidada.get('nuevaPassword'), 'utf-8')


            salt = gensalt()
            hashNuevaPassword = hashpw(nuevaPassword, salt).decode('utf-8')

            usuarioEncontrado.password = hashNuevaPassword

            conexion.session.commit()
            CambiarPassword(usuarioEncontrado.correo)
            return {
                'message': 'Contraseña actualizada exitosamente'
            }

        except Exception as error:
            return {
                'message': 'Error al actualizar la contraseña',
                'content': error.args
            }