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
    #p1 = Persona("Maria", "Diaz")
    #temasCurso = ["Algoritmos", "Base de Datos", "Python"]
# Voy a mostrar todas las materias que imparte la profesora y la hora que es.
    #ahora = datetime.datetime.now()
    asig = Asignatura

    return render(request, "registration/main.html", {"asignaturas": asig})
    #return render(request, "main.html", {"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "momento_actual": ahora, "temas_curso": temasCurso})

@login_required
def busqueda_mascotas(request):

    return render(request, "registration/busqueda_mascota.html")

@login_required
def buscar(request):

    if request.GET["mascotita"]:

        #mensaje = "Mascota Buscada: %r" %request.GET["mascotita"]
        mascota = request.GET["mascotita"]


        if len(mascota)>20:
            mensaje = "Texto de búsqueda demasiado largo"

        else:

            mascotas = Mascota.objects.filter(nombre__icontains=mascota)
            return render(request, "registration/resultados_busqueda.html", {"mascotas": mascotas, "query": mascota})
    else:

        mensaje = "No has introducido nada."

    return HttpResponse(mensaje)

@login_required
def contacto(request):

    if request.method=="POST":

        # El POST sirve para enviar un correoß
        return render(request, "registration/gracias.html")
    return render(request, "registration/contacto.html")

#def home(request):
#    return HttpResponse("Bienvenido")
