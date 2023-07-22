from flask import Flask, request
from datetime import datetime
from psycopg2 import connect
from uuid import UUID

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
        print(request.json)
        body = request.json
        cursor = conexion.cursor()

        cursor.execute("INSERT INTO categorias (nombre, estado, color) VALUES (%s, %s, %s)",
                       (body.get('nombre'), body.get('estado'), body.get('color')))
        conexion.commit()

        cursor.close()

        return {
            'message': 'Categoria creada exitosamente'
        }
    
@app.route('/categoria/<string:id>', methods=['GET', 'PUT'])
def manejoUnaCategoria(id):

    try:
        UUID(id, version=4)
    except ValueError:
         return{
    'message': 'Id no es UUID valido'
        }, 400 #Bad Request (mala solicitud)
    cursor = conexion.cursor()

    if request.method == 'GET':


        cursor.execute("SELECT * FROM categorias WHERE id = %s", (id,))
        resultado = cursor.fetchone()

        if not resultado:
            return {
                'message': 'La categoria no existe'
            }, 404 # Not Found (No encontrado)
        
        return {
            'content': {
                'id': resultado[0],
                'nombre': resultado[1],
                'estado': resultado[2],
                'color': resultado[3],
                'fechaCreacion': resultado[4]
            }
        }, 200 # Ok (Todo bien)
    elif request.method == 'PUT':
        body = request.json
        cursor.execute("UPDATE categorias SET nombre = %s, estado = %s, color =%s WHERE id = %s",
                       (body.get('nombre'), body.get('estado'), body.get('color'), id))
        
        conexion.commit()
        return {
            'message': 'Categoria actualizada exitosamente'
        }

if __name__ =='__main__':
    # si es el archivo principal, levantaremos el proyecto
    app.run(debug=True)