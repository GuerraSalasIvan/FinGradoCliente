import requests
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import *
import json

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


#------------------------- Buscar avanzado equipo-------------------------
def buscar_avanzado_equipo(request):
    if(len(request.GET) > 0):
        formulario = BusquedaAvanzadaEquipoForm(request.GET)
        
        try:
            headers = crear_cabecera()
            response = requests.get(
                'http://127.0.0.1:8000/api/v1/equipos/busqueda_avanzada',
                headers=headers,
                params=formulario.data
            )
            if(response.status_code == requests.codes.ok):
                equipos = response.json()
                return render(request, 'equipo/lista_equipos_api.html',
                              {"equipos_mostrar":equipos})
            else: 
                print(response.status_code)
                response.raise_for_status()
        except HTTPError as http_err:
            print(f'Hubo un error en la petición: {http_err}')
            if(response.status_code == 400):
                errores = response.json()
                for error in errores:
                    formulario.add_error(error,errores[error])
                return render(request, 'equipo/lista_equipos_api.html',
                            {"formulario":formulario, "errores":errores})
            else:
                return mi_error_500(request)
            
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
        
    else:
        formulario = BusquedaAvanzadaEquipoForm(None)
    return render(request, 'equipo/busqueda_avanzada.html', {'formulario':formulario})

#------------------------- Buscar avanzado ubicacion -------------------------
def buscar_avanzado_ubicacion(request):
    if(len(request.GET) > 0):
        formulario = BusquedaAvanzadaUbicacionForm(request.GET)
        
        try:
            headers = crear_cabecera()
            response = requests.get(
                'http://127.0.0.1:8000/api/v1/ubicacion/busqueda_avanzada',
                headers=headers,
                params=formulario.data
            )
            if(response.status_code == requests.codes.ok):
                ubicacion = response.json()
                return render(request, 'ubicacion/lista_ubicacion_api.html',
                              {"ubicacion_mostrar":ubicacion})
            else: 
                print(response.status_code)
                response.raise_for_status()
        except HTTPError as http_err:
            print(f'Hubo un error en la petición: {http_err}')
            if(response.status_code == 400):
                errores = response.json()
                for error in errores:
                    formulario.add_error(error,errores[error])
                return render(request, 'ubicacion/lista_ubicacion_api.html',
                            {"formulario":formulario, "errores":errores})
            else:
                return mi_error_500(request)
            
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
        
    else:
        formulario = BusquedaAvanzadaUbicacionForm(None)
    return render(request, 'ubicacion/busqueda_avanzada.html', {'formulario':formulario})



#------------------------- Buscar avanzado perfil publico -------------------------
def buscar_avanzado_perfil_publico(request):
    if(len(request.GET) > 0):
        formulario = BusquedaAvanzadaPerfil_PublicoForm(request.GET)
        
        try:
            headers = crear_cabecera()
            response = requests.get(
                'http://127.0.0.1:8000/api/v1/perfil_publico/busqueda_avanzada',
                headers=headers,
                params=formulario.data
            )
            if(response.status_code == requests.codes.ok):
                perfil_publico = response.json()
                return render(request, 'perfil_publico/lista_perfil_publico_api.html',
                              {"perfil_publico_mostrar":perfil_publico})
            else: 
                print(response.status_code)
                response.raise_for_status()
        except HTTPError as http_err:
            print(f'Hubo un error en la petición: {http_err}')
            if(response.status_code == 400):
                errores = response.json()
                for error in errores:
                    formulario.add_error(error,errores[error])
                return render(request, 'perfil_publico/busqueda_avanzada.html',
                            {"formulario":formulario, "errores":errores})
            else:
                return mi_error_500(request)
            
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
        
    else:
        formulario = BusquedaAvanzadaPerfil_PublicoForm(None)
    return render(request, 'perfil_publico/busqueda_avanzada.html', {'formulario':formulario})



def crear_equipo(request):
    if (request.method == "POST"):
        try:
            formulario = EquipoForm(request.POST)
            headers = {"Content-Type":"application/json"}
            
            datos = formulario.data

            
            response = requests.post(
                'http://127.0.0.1:8000/api/v1/equipos/crear',
                headers=headers,
                data=json.dumps(datos)
            )
            if(response.status_code == requests.codes.ok):
                return redirect("indice")
            else:
                print(response.status_code)
                response.raise_for_status()
        except HTTPError as http_err:
            print(f'Hubo un error en la petición: {http_err}')
            if(response.status_code == 400):
                errores = response.json()
                for error in errores:
                    formulario.add_error(error,errores[error])
                return render(request, 
                            'equipo/crear.html',
                            {"formulario":formulario})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
        
    else:
         formulario = EquipoForm(None)
    return render(request, 'equipo/crear.html',{"formulario":formulario})


def equipo_eliminar(request, equipo_id):
    try:
        headers = crear_cabecera()
        response = requests.delete(
            'http://127.0.0.1:8000/api/v1/equipos/eliminar/'+str(equipo_id),
            headers=headers,
        )
        if(response.status_code == requests.codes.ok):
            return redirect("indice")
        else:
            print(response.status_code)
            response.raise_for_status()
    except Exception as err:
        print(f'Ocurrió un error: {err}')
        return mi_error_500(request)
    return redirect('indice')
    
    
    #Páginas de Error
def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

#Páginas de Error
def mi_error_500(request,exception=None):
    return render(request, 'errores/500.html',None,None,500)