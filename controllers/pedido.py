from flask_restful import Resource, request
from utilitarios import conexion
from dtos import PedidoRequestDto
from flask_jwt_extended import get_jwt_identity
from decorators import validador_usuario_cliente
from models import PedidoModel, DetallePedidoModel


class PedidosController(Resource):
    @validador_usuario_cliente
    def post(self):
        data = request.get_json()
        try:
            dto = PedidoRequestDto()
            dataValidada = dto.load(data)
            usuarioId = get_jwt_identity()

            nuevoPedido = PedidoModel(usuarioId = usuarioId, total = 0.0)

            conexion.session.add(nuevoPedido)
            conexion.session.commit()
            detallePedidos = dataValidada.get('detallePedido')

            total = 0.0

            for detallePedido in detallePedidos:
                nuevoDetallePedido = DetallePedidoModel(
                                productoId = detallePedido.get('productoId'), 
                                cantidad = detallePedido.get('cantidad'),
                                precio = detallePedido.get('precio'),
                                subTotal = detallePedido.get('cantidad') * detallePedido.get('precio'),
                                pedidoId = nuevoPedido.id
)

                total += nuevoDetallePedido.subTotal
                conexion.session.add(nuevoDetallePedido)


            nuevoPedido.total = total
            conexion.session.commit()

            return {
                'message': 'Pedido creado correctamente'
            }, 201
        
        except Exception as error:
            conexion.session.rollback()
            return {
                'message': ' Error al crear el pedido',
                'content': error.args
            }
