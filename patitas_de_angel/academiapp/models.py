from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    dni_Responsable = models.CharField(max_length=20)
    nombre_Responsable = models.CharField(max_length=20)
    apellido_Responsable = models.CharField(max_length=20)

    def __str__(self):
        return f'Mascota {self.id} : {self.nombre} {self.especie} {self.raza} {self.dni_Responsable} {self.nombre_Responsable} {self.apellido_Responsable}'


class Asignatura(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    completado = models.BooleanField()
    pagado = models.BooleanField()
    mascota = models.ForeignKey(Mascota, on_delete=models.SET_NULL, null=True)
    #entrenadora = models.ForeignKey(Entrenadora, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Asignatura {self.id} : {self.nombre} {self.descripcion} {self.completado} {self.pagado}'


class Entrenadora(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    #pass1 = models.Charfield(max_length=10)
    asignatura = models.ForeignKey(
        Asignatura, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Entrenadora {self.id} : {self.nombre} {self.apellidos} {self.email} {self.pass1}'

# class Rol(models.Model):
#    rol = models.BooleanField()
#    persona = models.ForeignKey(
#        Persona,
#        on_delete=models.SET_NULL, null=True)

 #   def __str__(self):
  #      return f'Rol{self.id}: {self.rol}'

