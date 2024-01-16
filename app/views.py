import requests
from django.core import serializers
from django.shortcuts import render

def equipos_lista_api(request):
    response = requests.get('http://127.0.0.1:8000/api/v1/equipos')
    equipos = response.json()
    return render(request, 'equipo/lista_equipos_api.html',{'equipos_mostrar':equipos})