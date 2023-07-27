from flask import Flask
from base_de_datos import conexion
from models.usuario import UsuarioModel
from urllib.parse import quote_plus

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:%s@localhost:5432/directorio' % quote_plus('root')
conexion.init_app(app)

@app.route('/crear-tablas', methods=['GET'])
def crearTablas():
    conexion.create_all()
    return{
        'message': 'Creacion ejecutada exitosamente'
    }

if __name__ == '__main__':
    app.run(debug=True)