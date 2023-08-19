from django.urls import path
from .views import paginaInicio, devolverHoraServidor, CategoriasController, CategoriaController

urlpatterns = [
    path('inicio', paginaInicio),
    path('status', devolverHoraServidor),
    path('categorias', CategoriasController.as_view()),
    path('categoria/<id>', CategoriaController.as_view())
]