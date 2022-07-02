import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render

from academiapp.models import *

app_name='academiapp'
# Create your views here.

#class Persona(object):
#    def __init__(self, nombre, apellido):
#        self.nombre=nombre
#        self.apellido=apellido

#Para proteger nuestras vistas y que no cualquiera pueda acceder
@login_required
def home(request):
#    p1 = Persona("Maria", "Diaz")
#    temasCurso = ["Algoritmos", "Base de Datos", "Python"]
# Voy a mostrar todas las materias que imparte la profesora y la hora que es.
    ahora = datetime.datetime.now()
    asig = Asignatura

    return render(request, "main.html", {"asignaturas": asig})
#    return render(request, "main.html", {"nombre_persona": p1.nombre, "apellido_persona": p1.apellido,
#                                          "momento_actual": ahora, "temas_curso": temasCurso})

def busqueda_mascotas(request):

    return render(request, "busqueda_mascota.html")

def buscar(request):

    if request.GET["mascotita"]:

        #mensaje = "Mascota Buscada: %r" %request.GET["mascotita"]
        mascota = request.GET["mascotita"]
        mascotas = Mascota.objects.filter(nombre__icontains=mascota)

        return render(request, "resultados_busqueda.html", {"mascotas": mascotas, "query": mascota})

    else:

        mensaje = "No has introducido nada."

    return HttpResponse(mensaje)

#def home(request):
#    return HttpResponse("Bienvenido")
