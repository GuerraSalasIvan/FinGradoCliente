import requests
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import *

def equipos_lista_api(request):
    headers = {'Authorization': 'Bearer NOfsyzrO8gTjmWFg5dR0eoSB0UsPYI'}
    response = requests.get('http://127.0.0.1:8000/api/v1/equipos', headers=headers)
    equipos = response.json()
    return render(request, 'equipo/lista_equipos_api.html',{'equipos_mostrar':equipos})


def crear_cabecera():
    return {'Authorization': 'Bearer NOfsyzrO8gTjmWFg5dR0eoSB0UsPYI'}

def equipo_busqueda_simple(request):
    formulario = BusquedaequipoForm(request.GET)
    
    if formulario.is_valid():
        headers = crear_cabecera()
        response = requests.get(
            'http://127.0.0.1:8000/api/v1/busqueda/equipo_simple',
            headers=headers,
            params=formulario.cleaned_data
        )
        equipos = response.json()
        return render(request, 'equipo/lista_equipos_api.html',{"equipos_mostrar":equipos})
    if("HTTP_REFERER" in request.META):
        return redirect(request.META["HTTP_REFERER"])
    else:
        return redirect("indice")
    
from requests.exceptions import HTTPError