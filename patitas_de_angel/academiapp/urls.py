from django.contrib.auth import admin
from django.urls import path, include
from academiapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inicio', views.home, name='home')
   # path('', views.home, name='home'),
]