from django import forms

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