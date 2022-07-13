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


def crearUsuario(request):
    return render(request, "AppBlog/nuevoUsuario.html")


def contacto(request):
    return render(request, "AppBlog/contacto.html")