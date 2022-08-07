from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name='inicio'),
    path('admin/', admin),
    path('inicioSesion/', inicioSesion, name='inicioSesion'),
    path('CrearUsuario/', Crear_Usuario, name='CrearUsuario'),
    path('contacto/', contacto, name='contacto'),
    path('buscarUsuario/', buscarUsuario, name='buscarUsuario'),
    path('buscar/', buscar, name='buscar'),

    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='AppBlog/logout.html'), name='logout'),

    path('post/', post, name='post'),
]


