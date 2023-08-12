from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields, Schema
from models import UsuarioModel, TipoUsuario
from marshmallow_enum import EnumField

class UsuarioRequestDto(SQLAlchemyAutoSchema):
    # correo = auto_field()
    correo = fields.Email(required=True)
    class Meta:
        model = UsuarioModel

class UsuarioResponseDto(SQLAlchemyAutoSchema):
    tipoUsuario = EnumField(TipoUsuario)
    password = auto_field(load_only=True)

    class Meta:
        model = UsuarioModel

class LoginRequestDto(Schema):
    correo = fields.Email(required=True)
    password = fields.Str(required=True)

class CambiarPasswordRequestDto(Schema):
    password = fields.String(required=True)
    nuevaPassword = fields.String(required=True)