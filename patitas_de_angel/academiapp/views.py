import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render

#app_name='academiapp'


# Create your views here.
from academiapp.models import *


@login_required
def home(request):

    asig = Asignatura.objects.all()
    return render(request, "registration/main.html", {'asignaturas': asig})


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
