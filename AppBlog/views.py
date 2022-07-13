from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.models import *
# Create your views here.


def inicio(request):
    return render (request, "AppBlog/index.html")


def admin(request):
    return render(request, "AppBlog/nosotros.html")


def inicioSesion(request):
    return render(request, "AppBlog/inicioSesion.html")


def CrearUsuario(request):
    if request.method == 'POST':

        form = UsuarioForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            nombre_usuario = info["nombre_usuario"]
            email = info["email"]
            fecha_nacimiento = info["fecha_nacimiento"]
            contraseña = info["contraseña"]
            crearusuario = CrearUsuario(nombre=nombre, nombre_usuario=nombre_usuario, email=email, fecha_nacimiento=fecha_nacimiento, contraseña=contraseña)
            crearusuario.save()
            return render (request, "AppBlog/principal.html")
    else:
        form = UsuarioForm()
    return render(request, "AppBlog/CrearUsuario.html", {"form":form})       

def buscarUsuario(request):
    return render(request, "AppBlog/buscarUsuario.html")

def buscar(request):
    if request.get("nombre"):
        nombre=request.GET{'nombre'}
        crearusuario = CrearUsuario.objects.filter(nombre=nombre)
        return render(request, "AppBlog/resultado.html")
    nombre=request.GET{'nombre'}
    respuesta = f"Estoy buscando el usuario:   
    return httpResponse(respuesta)

def contacto(request):
    return render(request, "AppBlog/contacto.html")