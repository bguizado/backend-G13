from django.urls import path
from .views import paginaInicio, devolverHoraServidor, CategoriasController, CategoriaController,  GolosinasController, GolosinaController

urlpatterns = [
    path('inicio', paginaInicio),
    path('status', devolverHoraServidor),
    path('categorias', CategoriasController.as_view()),
    path('categoria/<id>', CategoriaController.as_view()),
    path('golosinas', GolosinasController.as_view()),
    path('golosina/<id>', GolosinaController.as_view())
]