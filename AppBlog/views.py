from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.models import *
# Create your views here.


def inicio(request):
    return render (request, "templates/index.html")


def admin(request):
    return render(request, "templates/nosotros.html")


def inicioSesion(request):
    return render(request, "templates/inicioSesion.html")


def crearUsuario(request):
    return render(request, "templates/nuevoUsuario.html")


def contacto(request):
    return render(request, "templates/contacto.html")