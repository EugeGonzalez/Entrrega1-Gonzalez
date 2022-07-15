from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.forms import *
from AppBlog.models import *
# Create your views here.


def inicio(request):
    return render (request, "AppBlog/index.html")


def admin(request):
    return render(request, "AppBlog/nosotros.html")


def inicioSesion(request):
    return render(request, "AppBlog/inicioSesion.html")


      

def buscarUsuario(request):
    return render(request, "AppBlog/buscarUsuario.html")

def buscar(request):
    if request.GET.get("nombre"):
        nombre=request.GET.get("nombre")
        usuario = CrearUsuario.objects.filter(nombre=nombre)
        return render(request, "AppBlog/resultado.html", {"usuario":usuario})
    else:
        return render(request, "AppBlog/buscarUsuario.html", {"error": "No se ingreso ningun dato"})

    

def contacto(request):
    if request.method == 'POST':

        form = contactoForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            
            contacto = Contacto(nombre=info["nombre"], email=info["email"],  numero_telefono=info["numero_telefono"])
            contacto.save()
            return render (request, "AppBlog/index.html")
    else:
        form = contactoForm()
    return render(request, "AppBlog/contacto.html", {"form":form})


def Crear_Usuario(request):
    if request.method == 'POST':

        form = UsuarioForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            
            crearusuario = CrearUsuario(nombre=info["nombre"], nombre_usuario=info["nombre_usuario"], email=info["email"], fecha_nacimiento=info["fecha_nacimiento"], contraseña=info["contraseña"])
            crearusuario.save()
            return render(request, "AppBlog/index.html")
    else:
        form = UsuarioForm()
    return render(request, "AppBlog/CrearUsuario.html", {"form":form})
    