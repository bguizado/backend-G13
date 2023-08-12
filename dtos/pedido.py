from marshmallow import Schema, fields

class DetallePedidoRequestDto(Schema):
    productoId = fields.Integer(required=True)
    cantidad = fields.Integer(required=True)
    precio = fields.Integer(required=True)


class PedidoRequestDto(Schema):
    detallePedido = fields.List(cls_or_instance = fields.Nested(nested = DetallePedidoRequestDto()))
