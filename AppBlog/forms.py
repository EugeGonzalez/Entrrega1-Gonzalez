from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import  User


class UsuarioForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    nombre_usuario=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=60)
    fecha_nacimiento=forms.DateField()
    contraseña= forms.CharField(max_length=30)

class contactoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=60)
    fecha_nacimiento=forms.DateField()
    numero_telefono=forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
        help_texts={k:"" for k in fields}

