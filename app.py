from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from controllers.usuario import LoginController
from utilitarios import conexion
from flask_cors import CORS
from os import environ
from dotenv import load_dotenv
from models import *
from flasgger import Swagger
from controllers import (CategoriaController, RegistroController, LoginController, SubirImagenController, DevolverImagenController, ProductosController, PedidosController, UsuarioController,CambiarPasswordController)
from flask_jwt_extended import JWTManager
from json import load
from datetime import timedelta

load_dotenv()
swaggerData = load(open('swagger_data.json', 'r'))

# https://github.com/flasgger/flasgger#customize-default-configurations
swaggerConfig = {
    'headers': [],
    'specs': [
        {
            'endpoint': '',
            'route': '/'
        }
    ],
    'static_url_path': '/flasgger_static',
    'specs_route': '/documentacion'
}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=environ.get('DATABASE_URL')

app.config['JWT_SECRET_KEY']=environ.get('JWT_SECRET')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1, minutes=15)

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

JWTManager(app)

Swagger(app, template=swaggerData, config=swaggerConfig)

CORS(app, origins='*')
api = Api(app)

api.add_resource(CategoriaController, '/categorias')
api.add_resource(RegistroController,'/registro' )
api.add_resource(LoginController, '/login' )
api.add_resource(SubirImagenController, '/subir-imagen')
api.add_resource(DevolverImagenController, '/imagenes/<nombreImagen>')
api.add_resource(ProductosController, '/productos')
api.add_resource(PedidosController, '/pedidos')
api.add_resource(UsuarioController, '/perfil')
api.add_resource(CambiarPasswordController, '/cambiar-password')


conexion.init_app(app)

Migrate(app, conexion)

if __name__ == '__main__':
    app.run(debug=True)