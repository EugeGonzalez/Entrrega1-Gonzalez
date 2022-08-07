from email.policy import default
from venv import create
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.db.models.signals import post_save



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Admin (models.Model):
    nombre_usuario = models.CharField(max_length=50)
    contraseña  = models.CharField(max_length= 30)
    tipo_usuario = models.CharField(max_length= 20)

    def __integer__(self):
        return self.nombre_usuario


class InicioSesion(models.Model):
    nombre_usuario=models.CharField(max_length=50)
    contraseña= models.CharField(max_length=30)




class CrearUsuario(models.Model):
    nombre=models.CharField(max_length=50)
    nombre_usuario=models.CharField(max_length=50)
    email=models.EmailField(max_length=60)
    fecha_nacimiento=models.DateField()
    contraseña= models.CharField(max_length=30)

    


class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField(max_length=60)
    numero_telefono=models.IntegerField()




class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'