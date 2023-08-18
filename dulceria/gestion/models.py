from django.db import models
from uuid import uuid4

class CategoriaModel(models.Model):

    opcionesNivelAzucar = (
        ['MUY_ALTO', 'MUY_ALTO'],
        ['ALTO','ALTO'],
        ['MEDIO', 'MEDIO'],
        ['BAJO', 'BAJO'],
        ['MUY_BAJO', 'MUY_BAJO'],
        ['CERO', 'CERO']
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.TextField(null=False)
    nivelAzucar = models.TextField(name='nivel_azucar', null=False, choices=opcionesNivelAzucar)

    class Meta:
        db_table = 'categorias'

class GolosinaModel(models.Model):

    tipoProcedencia = (
        ['NA', 'NACIONAL'],
        ['IMP','IMPORTADO']
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.TextField(null=False)
    fechaVencimiento = models.DateField(editable=False, null=False, name='fecha_vencimiento')
    precio = models.FloatField(null=False)
    procedencia = models.TextField(choices=tipoProcedencia, default='NACIONAL')
    categoria = models.ForeignKey(to=CategoriaModel, db_column='categoria_id', on_delete=models.PROTECT, related_name='golosinas')

    class Meta:
        db_table='golosinas'
        unique_together = [['nombre', 'fecha_vencimiento']]
