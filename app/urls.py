from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api', views.equipos_lista_api, name='indice'),
    path('equipo_busqueda_simple', views.equipo_busqueda_simple, name='equipo_busqueda_simple'),
    path('equipo/buscar_avanzado', views.buscar_avanzado_equipo, name='buscar_avanzado_equipo'),
]