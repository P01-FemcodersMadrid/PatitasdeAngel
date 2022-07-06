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

#class Curso(models.Model):
#    codigo = models.CharField(max_length=6, primary_key=True)
#    nombre = models.CharField(max_length=30)
#    descripcion = models.CharField(max_length=255)
#    entrenadora = models.CharField(max_length=100)

#class Mascota(models.Model):
 #   id_mascota = models.CharField(max_length=9, primary_key=True)
 #   nombre = models.CharField(max_length=40)
 #   fecha_nac = models.DateField()
 #   especie = models.CharField(max_length=40)
 #   raza = models.CharField(max_length=40)
 #   sexo = models.BooleanField()
 #   nombre_propietario = models.CharField(max_length=40)
 #   DNI_propietario = models.CharField(max_length=9)

 #   def __str__(self):
 #       return f'Mascota {self.id_mascota} : {self.nombre} {self.fecha_nac} {self.especie} {self.raza} {self.sexo} {self.nombre_propietarion} {self.DNI_propietario}'

#class


#class Matricula(models.Model):
#    id = models.AutoField(primary_key=True)
#    mascota

class Clienta(models.Model):

    dni_Responsable = models.CharField(max_length=20)
    nombre_Responsable = models.CharField(max_length=20)
    apellido_Responsable = models.CharField(max_length=20)
    email_Responsable = models.EmailField(max_length=30, default="name@yahoo.com")
    movil_Responsable = models.IntegerField(default=234567890)


    def __str__(self):
        return f'{self.dni_Responsable} {self.nombre_Responsable} {self.apellido_Responsable}'

#class Mascota(models.Model):
#    nombre = models.CharField(max_length=20)
#    especie = models.CharField(max_length=20)
#    raza = models.CharField(max_length=20)
#    clienta_id = models.ForeignKey(Clienta, on_delete=models.SET_NULL, null=True)
#    dni_Responsable = models.CharField(max_length=20)
#    nombre_Responsable = models.CharField(max_length=20)
#    apellido_Responsable = models.CharField(max_length=20)
#   email_Responsable = models.EmailField(max_length=30, default="name@yahoo.com")
 #   def __str__(self):
 #       return f'Mascota {self.id} : {self.nombre} {self.especie} {self.raza} {self.dni_Responsable} {self.nombre_Responsable} {self.apellido_Responsable} {self.email_Responsable}'

 #   def __str__(self):
 #       return f'{self.nombre} {self.especie} {self.raza} '



class Asignatura(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=100)
    completado = models.BooleanField()
    pagado = models.BooleanField()
 #   mascota = models.ForeignKey(Mascota, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nombre} {self.descripcion} {self.completado} {self.pagado}'


class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    clienta_id = models.ForeignKey(Clienta, on_delete=models.SET_NULL, null=True)
    asignatura_id = models.ForeignKey(Asignatura, on_delete=models.SET_NULL, null=True)
#    usuario_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
 #   user_id = User.ForeignKey(User, on_delete=User.SET_NULL, null=True)

#    dni_Responsable = models.CharField(max_length=20)
#    nombre_Responsable = models.CharField(max_length=20)
#    apellido_Responsable = models.CharField(max_length=20)
#   email_Responsable = models.EmailField(max_length=30, default="name@yahoo.com")
 #   def __str__(self):
 #       return f'Mascota {self.id} : {self.nombre} {self.especie} {self.raza} {self.dni_Responsable} {self.nombre_Responsable} {self.apellido_Responsable} {self.email_Responsable}'

    def __str__(self):
        return f'{self.nombre} {self.especie} {self.raza} '


#
#class Entrenadora(models.Model):
#    nombre = models.CharField(max_length=20)
#    apellidos = models.CharField(max_length=30)
#    email = models.CharField(max_length=30)
#    username = models.CharField(max_leghth=20)
#    password = models.CharField(max_length=20)
#    asignatura = models.ForeignKey(
#        Asignatura, on_delete=models.SET_NULL, null=True)

#    def __str__(self):
#       return f'Entrenadora {self.id} : {self.nombre} {self.apellidos} {self.email}'

# class Rol(models.Model):
#    rol = models.BooleanField()
#    persona = models.ForeignKey(
#        Persona,
#        on_delete=models.SET_NULL, null=True)

 #   def __str__(self):
  #      return f'Rol{self.id}: {self.rol}'

