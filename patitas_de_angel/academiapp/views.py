import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render

app_name='academiapp'
# Create your views here.

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

#Para proteger nuestras vistas y que no cualquiera pueda acceder
@login_required
def home(request):
    p1 = Persona("Maria", "Diaz")
    temasCurso = ["Algoritmos", "Base de Datos", "Python"]
    ahora = datetime.datetime.now()
    return render(request, "main.html", {"nombre_persona": p1.nombre, "apellido_persona": p1.apellido,
                                          "momento_actual": ahora, "temas_curso": temasCurso})
#def home(request):
#    return HttpResponse("Bienvenido")
