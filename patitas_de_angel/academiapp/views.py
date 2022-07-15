import datetime
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render, redirect, get_object_or_404
from academiapp.models import *

# Create your views here.

@login_required
def home(request):
    mas = Mascota.objects.all()
    return render(request, "registration/main.html", {'mascotas': mas})

@login_required
def detalleMascota(request, id):
    mascota = Mascota.objects.get(pk=id)
    return render(request, 'registration/detalleMascota.html', {'mascota': mascota})

@login_required
def editarMascota(request, id):
    mascota = get_object_or_404(Mascota, pk=id)
    if request.method == 'POST':
        formaMascota = MascotaForm(request.POST, instance=mascota)
        if formaMascota.is_valid():
            formaMascota.save()
            messages.success(request, "Modificado correctamente")
            return redirect('home')
    else:
          #pasa la informacion del objeto recuperado de nuestra base de datos
          # recibe una referencia de nuestro modelo formulario que llama a nuestra clase persona
          # usamos instance para indicar el objeto que vamos a trabajar en el formulario
        formaMascota = MascotaForm(instance=mascota)

    return render(request, 'registration/editarMascota.html', {'formaMascota': formaMascota})

@login_required
def eliminarMascota(request, id):
    mascota = Mascota.objects.get(id=id)
    #POST request
    if request.method == "POST":
        #Confirma eliminar
        mascota.delete()
        messages.success(request, "Registro eliminado correctamente.")
        return redirect('home')
    return render(request, "registration/eliminarMascota.html", {'mascota': mascota})

@login_required
def listarMascotas(request):

    masc = Mascota.objects.all()
    return render(request, "registration/listarMascotas.html", {'mascotas': masc})

@login_required
def nuevaMascota(request):
    if request.method == 'POST':
        formaMascota = MascotaForm(request.POST)
        if formaMascota.is_valid():
            formaMascota.save()
            messages.success(request, "Registro de Mascota agregado correctamente.")
            return redirect('home')
        else:
            messages.error(request, "Falta ingresar datos.")
    else:
        formaMascota = MascotaForm

    return render(request, 'registration/nuevaMascota.html', {'formaMascota': formaMascota})


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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            context = messages.success(request, f'Usuario {username} creado')
            return redirect('/', context)
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/registrar.html', context)


