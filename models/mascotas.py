from sqlalchemy import Column, types, ForeignKey
from base_de_datos import conexion
from enum import Enum

class TipoMascota(Enum):
    Perro = 'Perro'
    Gato = 'Gato'
    Cuy = 'Loro'

class SexoMascota(Enum):
    Macho = 'Macho'
    Hembra = 'Hembra'
    Helicoptero = 'Helicoptero'
    Otro = 'Otro'

class MascotaModel(conexion.Model):

    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    tipo = Column(type_=types.Enum(TipoMascota), nullable=False)
    sexo = Column(type_=types.Enum(SexoMascota), default=SexoMascota.Otro)
    fechaNacimiento = Column(type_=types.Date, name='fecha_nacimiento')
    usuarioId = Column(ForeignKey(column='usuarios.id'), nullable=False, name='usuario_id')


    __tablename__ = 'mascotas'