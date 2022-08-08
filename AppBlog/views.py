from email import message
from http.client import HTTPResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from AppBlog.forms import *
from AppBlog.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def inicio(request):
    post = Post.objects.all()

    context = { 'posts': post}
    return render (request, "AppBlog/index.html")

def profile(request):
    return render(request, 'AppBlog/profile.html')


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
    


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid:
            usuario=request.POST['username']
            clave=request.POST['password']

            user=authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, 'AppBlog/index.html', {'form':form, 'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, 'AppBlog/login.html', {'form':form, 'mensaje':f"Datos incorrectos"})
        else:
            return render(request, 'AppBlog/login.html', {'form':form, 'mensaje':f"Formulario incorrecto"})
    else:
        form=AuthenticationForm()
        return render(request,'AppBlog/login.html', {'form':form})



def register(request):
    if request.method=='POST':

        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request, 'AppBlog/index.html', {'form':form, 'mensaje':f"Usuario creado: {username}"})
    else:
        form=UserRegisterForm()
    return render(request, 'AppBlog/register.html', {'form':form})

def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            message.success(request, 'Post realizado')
            return render(request, 'AppBlog/index.html', {'form':form})
    else:
        form = PostForm()
    return render(request, 'AppBlog/index.html', {'form':form})