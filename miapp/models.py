from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Desarrolladores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    especialidades = models.TextField(default=None)
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Propuestas(models.Model):
    titulo = models.CharField(max_length=50)
    desarrollo= models.TextField(default=None)
    contacto=models.TextField(default=None)
    fechaSolicitud = models.DateField(default=timezone.now)

class Posteos(models.Model):
    titulo = models.CharField(max_length=50)
    desarrollo= models.TextField(default=None)
    fechaSolicitud = models.DateField(default=timezone.now)
    email = models.EmailField()

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.imagen}]"


