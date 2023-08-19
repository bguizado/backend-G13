from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from rest_framework.request import Request
from rest_framework.views import APIView
from .models import CategoriaModel
from .serializers import CategoriaSerializer
from rest_framework import status


# Create your views here.
# Ejemplo de como renderizar plantillas

def paginaInicio(request):
    print(request)

    data = {
        'usuario': {
            'nombre': 'Brando',
            'apellido': 'Guizado'
        },
        'hobbies': [
            {
                'descripcion': 'Ir al cine'
            },
            {
                'descripcion': 'Escuchar musica'
            }
        ]
    }

    return render(request, 'inicio.html', {'data': data})

@api_view(http_method_names=['GET', 'POST'])
def devolverHoraServidor(request: Request):
    print(request.method)

    if request.method == 'GET':

        return Response(data={
            'content': datetime.now()
        })
    elif request.method == 'POST':
        return Response(data={
            'content': 'Para saber la hora, realiza un GET'
        })
    
class CategoriasController(APIView):
    def get(self, request):
        #SELECT FROM * categorias;
        categorias = CategoriaModel.objects.all()
        print(categorias)
        serializador = CategoriaSerializer(instance=categorias, many= True)
        return Response(data={
            'message': 'La categoria es`',
            'content': serializador.data
        })
    
    def post(self, request:Request):
        data = request.data
        serializador = CategoriaSerializer(data= data)
        validacion = serializador.is_valid()
        if validacion == True:
            nuevaCategoria = serializador.save()
            print(nuevaCategoria)
            return Response(data={
                'message': 'Categoria creada exitosamente'
            }, status = status.HTTP_201_CREATED)
        else:
            return Response(data={
            'message': 'Error al crear la categoria',
            'content': serializador.errors
        }, status= status.HTTP_400_BAD_REQUEST)

class CategoriaController(APIView):
    def get(self, request: Request, id: str):
        categoriaEncontrada = CategoriaModel.objects.filter(id = id).first()
        if not categoriaEncontrada:
            return Response ( data= {
                'message': 'Categoria no encontrada'
            }, status=status.HTTP_404_NOT_FOUND)
        serializador = CategoriaSerializer(instance=categoriaEncontrada)
        return Response(data={
            'content': serializador.data
        })
    
    def put(self, request:Request, id:str):
        categoriaEncontrada = CategoriaModel.objects.filter(id = id).first()
        if not categoriaEncontrada:
            return Response ( data= {
                'message': 'Categoria no encontrada'
            }, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        serializador = CategoriaSerializer(data=data)
        dataValida = serializador.is_valid()
        if dataValida:
            serializador.validated_data
            serializador.update(categoriaEncontrada, serializador.validated_data)
            return Response( data= {
                'message': 'Categoria actualizada exitosamente'
            }, status=status.HTTP_200_OK)
        else: 
            return Response(data={
                'message': ' Error al actualizar la categoria',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request:Request, id:str):
        categoriaEncontrada = CategoriaModel.objects.filter(id = id).first()
        if not categoriaEncontrada:
            return Response ( data= {
                'message': 'Categoria no encontrada'
            }, status=status.HTTP_404_NOT_FOUND)
        
        CategoriaModel.objects.filter(id=id).delete()

        return Response(data={
            'message': 'Categoria eliminada exitosamente'
        })