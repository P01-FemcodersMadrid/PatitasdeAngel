from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

class Clienta(models.Model):

    dni_Responsable = models.CharField(max_length=20)
    nombre_Responsable = models.CharField(max_length=20)
    apellido_Responsable = models.CharField(max_length=20)
    email_Responsable = models.EmailField(max_length=30, default="name@yahoo.com")
    movil_Responsable = models.IntegerField(default=234567890)


    def __str__(self):
        return f'{self.dni_Responsable} {self.nombre_Responsable} {self.apellido_Responsable}'

class Asignatura(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=100)
    completado = models.BooleanField()
    pagado = models.BooleanField()

    def __str__(self):
        return f'{self.nombre} {self.descripcion} {self.completado} {self.pagado}'


class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    clienta_id = models.ForeignKey(Clienta, on_delete=models.SET_NULL, null=True)
    asignatura_id = models.ForeignKey(Asignatura, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nombre} {self.especie} {self.raza} '

