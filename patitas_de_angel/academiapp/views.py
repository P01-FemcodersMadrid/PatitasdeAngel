from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
app_name= 'academiapp'
# Create your views here.

#Para proteger nuestras vistas y que no cualquiera pueda acceder
@login_required
def home(request):
    return HttpResponse("Bienvenido")
