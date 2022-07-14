from django.db import models



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
