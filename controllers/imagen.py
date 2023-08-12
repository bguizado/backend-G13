from flask_restful import Resource, request
from decorators import validador_usuario_admin
from werkzeug.utils import secure_filename
from os import path
from datetime import datetime
from flask import send_file

class SubirImagenController(Resource):
    @validador_usuario_admin
    def post(self):
        """
        file: controllers/subirImagenSwagger.yml
        """   
        imagen = request.files.get('imagen')
        mimetypeValidos = ['image/png', 'image/jpeg', 'image/svg+xml']
        if not imagen:
            return {
                'message': 'Se necesita una imagen'
            },400

        print(imagen.filename) #nombre del archivo
        print(imagen.name) # nombre de la llave de mi form-data
        print(imagen.mimetype) #nombre extension del archivo
        if imagen.mimetype not in mimetypeValidos:
            return {
                'message': 'El archivo solo puede ser .jpg, .png, .svg'
            }, 400
        
        id = datetime.now().strftime('%f')

        filename = id + secure_filename(imagen.filename)

        ruta = path.join('imagenes', filename)
        imagen.save(ruta)
        return {
            'message': 'Imagen subida exitosamente',
            'content': {
                'imagen': f'imagenes/{filename}'
            }
        }
    
class DevolverImagenController(Resource):
    def get(self, nombreImagen):
        ruta = path.join('imagenes', nombreImagen)
        resultado = path.isfile(ruta)
        if not resultado:
            return {
                'message': 'El archivo a buscar no existe'
            }, 404

        print(nombreImagen)
        print(resultado)
        return send_file(ruta)