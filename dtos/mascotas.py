from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.mascotas import MascotaModel

class MascotaRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = MascotaModel
        include_fk = True