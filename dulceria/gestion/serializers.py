from rest_framework import serializers
from .models import CategoriaModel, GolosinaModel

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = '__all__'
        # fields = ['id', 'nombre', 'nivelAzucar']
        # exclude = ['id']

class GolosinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GolosinaModel
        fields = '__all__'


class GolosinaResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GolosinaModel
        fields = '__all__'
        depth = 1

class CategoriaResponseSerializer(serializers.ModelSerializer):

    golosinass = GolosinaSerializer(many=True, source='golosinas')

    class Meta:
        model = CategoriaModel
        fields = '__all__'