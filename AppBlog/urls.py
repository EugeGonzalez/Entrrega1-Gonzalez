from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('admin/', admin),
    path('inicioSesion/', inicioSesion, name='inicioSesion'),
    path('CrearUsuario/', CrearUsuario, name='CrearUsuario'),
    path('contacto/', contacto, name='contacto'),
    path('buscarUsuario/', buscarUsuario, name='buscarUsuario'),
    path('buscar/', buscar),
]

