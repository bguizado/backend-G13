from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
from models import ProductModel
from dtos import CategoriaRequestDto

class ProductoRquestDto(SQLAlchemyAutoSchema):
    class Meta:
        model= ProductModel
        include_fk = True


class ProductoResponseDto(SQLAlchemyAutoSchema):
    categoria = fields.Nested(CategoriaRequestDto)
    
    class Meta:
        model= ProductModel

