from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PosteosForm(forms.Form):
    titulo = forms.CharField(label="Título",max_length=50,required=True)
    desarrollo= forms.CharField(label="Desarrollo",max_length=500,required=True)
    fechaSolicitud = forms.DateField(label="Fecha de la Solicitud", required=False)
    email = forms.EmailField(label="Email")

class PropuestasForm(forms.Form):
    titulo = forms.CharField(label="Título",max_length=50,required=True)
    desarrollo= forms.CharField(label="desarrollo",max_length=500,required=True)
    contacto=forms.EmailField(label="Email")
    fechaSolicitud = forms.DateField(label="Fecha de la Solicitud", required=False)

class DesarrolladoresForm(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=50,required=True)
    apellido = forms.CharField(label="Apellido",max_length=50,required=True)
    email = forms.EmailField(label="Email")
    especialidades = forms.CharField(label="Especialidades",max_length=500,required=True)

class ClientesForm(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=50,required=True)
    apellido = forms.CharField(label="Apellido",max_length=50,required=True)
    email = forms.EmailField(label="Email")


class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}    

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name' ] 
        #Saca los mensajes de ayuda
        help_texts = { k:"" for k in fields}

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)        