from flask_restful import Resource, request
from models import ProductModel, CategoriaModel
from decorators import validador_usuario_admin
from dtos import ProductoRquestDto, ProductoResponseDto
from utilitarios import conexion

class ProductosController(Resource):

    @validador_usuario_admin
    def post(self):
        data = request.get_json()
        dto = ProductoRquestDto()
        try:
            dataValidada = dto.load(data)

            nuevoProducto = ProductModel(**dataValidada)

            conexion.session.add(nuevoProducto)
            conexion.session.commit()
            dtoRpta = ProductoResponseDto()

            return {
                'message': 'Producto creado exitosamente',
                'content': dtoRpta.dump(nuevoProducto)
            }
        
        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'Error al crear el producto',
                'content': error.args
            }
        

    def get(self):
        productoEncontrados = conexion.session.query(ProductModel).all()

        data = conexion.session.query(ProductModel).join(CategoriaModel).with_entities(ProductModel.id, CategoriaModel.id, CategoriaModel.nombre).all()
        print(conexion.session.query(ProductModel).join(CategoriaModel).with_entities(ProductModel.id, CategoriaModel.id, CategoriaModel.nombre))
        

        print(data[0])
        dto = ProductoResponseDto()

        return {
            'content': dto.dump(productoEncontrados, many=True)
        }