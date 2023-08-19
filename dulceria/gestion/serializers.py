from rest_framework import serializers
from .models import CategoriaModel

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = '__all__'
        # fields = ['id', 'nombre', 'nivelAzucar']
        # exclude = ['id']