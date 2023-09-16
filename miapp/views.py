from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "miapp/base.html")

def clientes(request):
    ctx={"clientes": Clientes.objects.all()}
    return render(request, "miapp/clientes.html",ctx)

class ClientesList(LoginRequiredMixin, ListView):
    model = Clientes

class DesarrolladoresList(LoginRequiredMixin, ListView):
    model = Desarrolladores

def desarrolladores(request):
    ctx={"desarrolladores": Desarrolladores.objects.all()}
    return render(request, "miapp/desarrolladores.html",ctx)

def propuestas(request):
    ctx={"propuestas": Propuestas.objects.all()}
    return render(request, "miapp/propuestas.html",ctx)

def posteos(request):
    ctx={"posteos": Posteos.objects.all()}
    return render(request, "miapp/posteos_list.html",ctx)



def propuestasForm(request):
    if request.method == "POST": 
       miForm = PropuestasForm(request.POST)
       if miForm.is_valid():
           titulo_p=miForm.cleaned_data.get('titulo')
           desarrollo_p=miForm.cleaned_data.get('desarrollo')
           contacto_p=miForm.cleaned_data.get('contacto')
           fechaSolicitud_p=miForm.cleaned_data.get('fechaSolicitud')
           propuesta=Propuestas(titulo=titulo_p, descripcion=desarrollo_p,fechaSolicitud=fechaSolicitud_p)
           propuesta.save()
           return render(request, "miapp/base.html")
    else:
      miForm = PropuestasForm()
    return render(request,"miapp/propuestasForm.html", {"form":miForm})

def desarrolladoresForm(request):
    if request.method == "POST": 
       miForm = DesarrolladoresForm(request.POST)
       if miForm.is_valid():
           nombre_d=miForm.cleaned_data.get('nombre')
           apellido_d=miForm.cleaned_data.get('apellido')
           email_d=miForm.cleaned_data.get('email')
           especialidades_d=miForm.cleaned_data.get('especialidades')
           desarrollador=Desarrolladores(nombre=nombre_d, apellido=apellido_d,email=email_d,especialidades=especialidades_d)
           desarrollador.save()
           return render(request, "miapp/base.html")
    else:
      miForm = DesarrolladoresForm()
    return render(request,"miapp/desarrolladoresForm.html", {"form":miForm})

def clientesForm(request):
    if request.method == "POST": 
       miForm = ClientesForm(request.POST)
       if miForm.is_valid():
           nombre_c=miForm.cleaned_data.get('nombre')
           apellido_c=miForm.cleaned_data.get('apellido')
           email_c=miForm.cleaned_data.get('email')
           cliente=Clientes(nombre=nombre_c, apellido=apellido_c,email=email_c)
           cliente.save()
           return render(request, "miapp/base.html")
    else:
      miForm = ClientesForm()
    return render(request,"miapp/clientesForm.html", {"form":miForm})

def buscarPropuesta(request):
   return render(request,"miapp/buscar_propuesta.html")

def resultadosPropuesta(request):
    if request.GET['titulo']:
        titulo = request.GET['titulo']
        propuesta = Propuestas.objects.filter(titulo__icontains=titulo)
        return render(request, 
                      "miapp/resultadosPropuesta.html", 
                      {"titulo": titulo, "propuestas":propuesta})
    return HttpResponse("No se ingresaron datos a buscar!")


class PosteosList(LoginRequiredMixin, ListView):
    model = Posteos

class PosteosCreate(LoginRequiredMixin, CreateView):
    model = Posteos
    fields = ['titulo', 'desarrollo', 'fechaSolicitud','email']
    success_url = reverse_lazy('miapp:posteos')

class PosteosDetail(LoginRequiredMixin, DetailView):
    model = Posteos

class PosteosUpdate(LoginRequiredMixin, UpdateView):
    model = Posteos
    fields = ['titulo', 'desarrollo', 'fechaSolicitud','email']
    success_url = reverse_lazy('miapp:posteos')    

class PosteosDelete(LoginRequiredMixin, DeleteView):
    model = Posteos
    success_url = reverse_lazy('miapp:posteos')    




class PropuestasList(LoginRequiredMixin, ListView):
    model = Propuestas

class PropuestasCreate(LoginRequiredMixin, CreateView):
    model = Propuestas
    fields = ['titulo', 'desarrollo', 'contacto','fechaSolicitud']
    success_url = reverse_lazy('miapp:propuestas')    

class PropuestasDetail(LoginRequiredMixin, DetailView):
    model = Propuestas

class PropuestasUpdate(LoginRequiredMixin, UpdateView):
    model = Propuestas
    fields = ['titulo', 'desarrollo', 'contacto','fechaSolicitud']
    success_url = reverse_lazy('miapp:propuestas')    

class PropuestasDelete(LoginRequiredMixin, DeleteView):
    model = Propuestas
    success_url = reverse_lazy('miapp:propuestas')   


def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
    #_____________________                
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.png'
                finally:
                    request.session['avatar'] = avatar

                return render(request, "miapp/base.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "miapp/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})
        else:    
            return render(request, "miapp/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})

    miForm = AuthenticationForm()

    return render(request, "miapp/login.html", {"form":miForm})    

def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST) # UserCreationForm 
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "miapp/base.html", {"mensaje":"Usuario Creado"})        
    else:
        form = RegistroUsuariosForm() # UserCreationForm 

    return render(request, "miapp/registro.html", {"form": form})   

#_________________ Registración de usuarios
# 

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "miapp/base.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
        else:
            return render(request, "miapp/editarPerfil.html", {'form': form})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "miapp/editarPerfil.html", {'form': form, 'usuario':usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            #_________________ Esto es para borrar el avatar anterior
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0: # Si esto es verdad quiere decir que hay un Avatar previo
                avatarViejo[0].delete()

            #_________________ Grabo avatar nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            #_________________ Almacenar en session la url del avatar para mostrarla en base
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "miapp/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "miapp/agregarAvatar.html", {'form': form})


