"""patitas_de_angel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from academiapp import urls
from django.contrib.auth import views as auth_views
from academiapp import views
from academiapp.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('academiapp.urls')),
    path('index', views.index),
    path('busqueda_mascotas', views.busqueda_mascotas),
    path('buscar/', views.buscar),
    path('nuevaMascota', views.nuevaMascota),
    path('listarMascotas', views.listarMascotas),
    path('registration/detalleMascota/<int:id>', views.detalleMascota),
    path('registration/editarMascota/<int:id>', views.editarMascota),
    path('registration/eliminarMascota/<int:id>', views.eliminarMascota),
    path('contacto/', views.contacto),
    path('registrar', register, name="registrar"),
    path('accounts/', include('django.contrib.auth.urls')),
]
