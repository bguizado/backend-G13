from flask import Flask, request
from datetime import datetime
from psycopg2 import connect

conexion = connect(database="minimarket", user="postgres", password="root", host="localhost", port="5432")


# __name__ = indicara si es el archivo en el cual estamos es el archivo principal o no (__main__)
app = Flask(__name__)


#indicando que la ruta '/' aceptara GET y POST
@app.route('/', methods = ['GET', 'POST'])
def inicio():
    #request = se guardara toda la informacion que me envia el cliente (FE)
    print(request.method)
    if request.method == 'GET':
        return {
            'message': 'Bienvenido a mi API de Flask'
        }
    elif request.method == 'POST':
        return {
            'message': 'La hora del servidor es : %s'% (datetime.now())
        }

@app.route('/categorias', methods = ['GET', 'POST'])
def manejoCategorias():
    if request.method == 'GET':
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM categorias;")

        data = cursor.fetchall()

        cursor.close()


        resultado = []

        for categoria in data:
            
            dataCategoria = {
                'id': categoria[0],
                'nombre': categoria[1],
                'estado': categoria[2],
                'color': categoria[3],
                'fechaCreacion': categoria[4]
            }
            resultado.append(dataCategoria)
            print(dataCategoria)
        return {
            'content': resultado
        }

    elif request.method == 'POST':
        return {
            'message': 'Categoria creada exitosamente'
        }
if __name__ =='__main__':
    # si es el archivo principal, levantaremos el proyecto
    app.run(debug=True)