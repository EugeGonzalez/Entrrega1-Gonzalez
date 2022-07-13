from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio),
    path('admin/', admin),
    path('inicioSesion/', inicioSesion),
    path('crearUsuario/', crearUsuario),
    path('contacto/', contacto),
]

