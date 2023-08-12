
from functools import wraps
from flask_jwt_extended.view_decorators import verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError
from models import UsuarioModel, TipoUsuario
from utilitarios import conexion


def validador_usuario_admin(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        data = verify_jwt_in_request()
        id = data[1].get('sub')
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()

        if not usuarioEncontrado:
            raise NoAuthorizationError('El usuario no existe')
        
        print(usuarioEncontrado.tipoUsuario)
        if usuarioEncontrado.tipoUsuario != TipoUsuario.ADMIN:
            raise NoAuthorizationError('El usuario no tiene permisos suficientes')

        return funcion(*args, *kwargs)
    return wrapper

def validador_usuario_cliente(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        data = verify_jwt_in_request()
        id = data[1].get('sub')
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()

        if not usuarioEncontrado:
            raise NoAuthorizationError('El usuario no existe')
        
        print(usuarioEncontrado.tipoUsuario)
        if usuarioEncontrado.tipoUsuario != TipoUsuario.CLIENTE:
            raise NoAuthorizationError('El usuario no tiene permisos suficientes')

        return funcion(*args, *kwargs)
    return wrapper