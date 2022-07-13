from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('admin/', admin),
    path('inicioSesion/', inicioSesion, name='inicioSesion'),
    path('crearUsuario/', crearUsuario, name='crear'),
    path('contacto/', contacto, name='contacto'),
]

