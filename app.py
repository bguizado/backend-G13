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
from controllers import CategoriaController, RegistroController
from json import load

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

Swagger(app, template=swaggerData, config=swaggerConfig)

CORS(app, origins='*')
api = Api(app)

api.add_resource(CategoriaController, '/categorias')
api.add_resource(RegistroController,'/registro' )
api.add_resource(LoginController, '/login' )

conexion.init_app(app)

Migrate(app, conexion)

if __name__ == '__main__':
    app.run(debug=True)