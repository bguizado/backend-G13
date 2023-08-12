from sqlalchemy import Column, types, ForeignKey
from utilitarios import conexion
from datetime import datetime
from sqlalchemy.orm import relationship

class ProductModel(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement= True)
    nombre = Column(type_=types.Text, nullable=False)
    descripcion = Column(type_=types.Text, nullable=True)
    precio = Column(type_=types.Float, nullable=False)
    precioDscto = Column(type_=types.Float, nullable=True, name='precio_dscto')
    imagen = Column(type_=types.Text)
    disponibilidad = Column(type_=types.Boolean, default=True)
    stock = Column(type_=types.Integer, nullable=False)
    categoriaId = Column(ForeignKey(column='categorias.id'), nullable=True, name='categoria_id')
    
    categoria = relationship('CategoriaModel', backref='productos')

    __tablename__='productos'