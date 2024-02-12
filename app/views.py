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

def ubicacion_lista_api(request):
    headers = {'Authorization': 'Bearer NOfsyzrO8gTjmWFg5dR0eoSB0UsPYI'}
    response = requests.get('http://127.0.0.1:8000/api/v1/ubicacion', headers=headers)
    ubicacion = response.json()
    return render(request, 'ubicacion/lista_ubicacion_api.html',{'ubicacion_mostrar':ubicacion})

def perfil_publico_lista_api(request):
    headers = {'Authorization': 'Bearer NOfsyzrO8gTjmWFg5dR0eoSB0UsPYI'}
    response = requests.get('http://127.0.0.1:8000/api/v1/perfil_publico', headers=headers)
    perfil_publico = response.json()
    return render(request, 'perfil_publico/lista_perfil_publico_api.html',{'perfil_publico_mostrar':perfil_publico})


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


def equipo_obtener(request, equipo_id):
    equipo = helper.obtener_equipo(equipo_id)
    return render (request, 'equipo/equipo.html',{"equipo":equipo})

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


def equipo_editar(request, equipo_id):
    
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    equipo = helper.obtener_equipo(equipo_id)
    formulario = EquipoForm(datosFormulario,
                        initial={
                            'id':equipo['id'],
                            'nombre':equipo['nombre'],
                            'deporte':equipo["deporte"]['id'],
                            'liga':equipo["liga"]['id'],
                            'capacidad':equipo['capacidad'],
                            'usuario':equipo['usuario'], # mirar esto (for ...)
                            
                        })
    if (request.method == "POST"):
        try:
            formulario = EquipoForm(request.POST)
            headers = {"Content-Type":"application/json"}
            datos = request.POST.copy()
            datos["usuarios"] = request.POST.getlist("usuarios")
            datos["deporte"] = request.POST.getlist("deporte")
            
            response = requests.put(
                'http://127.0.0.1:8000/api/v1/equipos/editar/'+str(equipo_id),
                headers=headers,
                data=json.dumps(datos)
            )
            if(response.status_code == requests.codes.ok):
                return redirect("equipo_obtener",equipo_id=equipo_id)
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
                            'equipo/actualizar.html',
                            {"formulario":formulario,"equipo":equipo})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
    return render(request, 'equipo/actualizar.html',{"formulario":formulario,"equipo":equipo})


def equipo_editar_nombre(request,equipo_id):
   
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    equipo = helper.obtener_equipo(equipo_id)
    formulario = EquipoActualizarNombreForm(datosFormulario,
            initial={
                'nombre': equipo['nombre'],
            }
    )
    if (request.method == "POST"):
        try:
            formulario = EquipoForm(request.POST)
            headers = crear_cabecera()
            datos = request.POST.copy()
            response = requests.patch(
                'http://127.0.0.1:8000/api/v1/equipos/editar/nombre/'+str(equipo_id),
                headers=headers,
                data=json.dumps(datos)
            )
            if(response.status_code == requests.codes.ok):
                return redirect("equipo_mostrar",equipo_id=equipo_id)
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
                            'equipo/actualizar_nombre.html',
                            {"formulario":formulario,"equipo":equipo})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
    return render(request, 'equipo/actualizar_nombre.html',{"formulario":formulario,"equipo":equipo})
    
            
        
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

def ubicacion_obtener(request, ubicacion_id):
    ubicacion = helper.obtener_ubicacion(ubicacion_id)
    return render (request, 'ubicacion/ubicacion.html',{"ubicacion":ubicacion})

def crear_ubicacion(request):
    if (request.method == "POST"):
        try:
            formulario = UbicacionForm(request.POST)
            headers = {"Content-Type":"application/json"}
            
            datos = formulario.data

            
            response = requests.post(
                'http://127.0.0.1:8000/api/v1/ubicacion/crear',
                headers=headers,
                data=json.dumps(datos)
            )
            if(response.status_code == requests.codes.ok):
                return redirect("ubicacion")
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
                            'ubicacion/crear.html',
                            {"formulario":formulario})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
        
    else:
         formulario = UbicacionForm(None)
    return render(request, 'ubicacion/crear.html',{"formulario":formulario})

def ubicacion_editar(request, ubicacion_id):
    
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    ubicacion = helper.obtener_ubicacion(ubicacion_id)
    formulario = UbicacionForm(datosFormulario,
                        initial={
                            'id':ubicacion['id'],
                            'nombre':ubicacion['nombre'],
                            'capacidad':ubicacion['capacidad'],
                            'deporte':ubicacion["deporte"],
                            'equipo':ubicacion['equipo'], 
                            
                        })
    if (request.method == "POST"):
        try:
            formulario = UbicacionForm(request.POST)
            headers = {"Content-Type":"application/json"}
            datos = request.POST.copy()
            datos["equipo"] = request.POST.getlist("equipo")
            datos["deporte"] = request.POST.getlist("deporte")
            
            response = requests.put(
                'http://127.0.0.1:8000/api/v1/ubicacion/editar/'+str(ubicacion_id),
                headers=headers,
                data=json.dumps(datos)
            )
            if(response.status_code == requests.codes.ok):
                return redirect("ubicacion_obtener",ubicacion_id=ubicacion_id)
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
                            'ubicacion/actualizar.html',
                            {"formulario":formulario,"ubicacion":ubicacion})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
    return render(request, 'ubicacion/actualizar.html',{"formulario":formulario,"ubicacion":ubicacion})

def ubicacion_editar_nombre(request,ubicacion_id):
   
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    ubicacion = helper.obtener_ubicacion(ubicacion_id)
    formulario = UbicacionActualizarNombreForm(datosFormulario,
            initial={
                'nombre': ubicacion['nombre'],
            }
    )
    if (request.method == "POST"):
        try:
            formulario = UbicacionForm(request.POST)
            headers = crear_cabecera()
            datos = request.POST.copy()
            response = requests.patch(
                'http://127.0.0.1:8000/api/v1/ubicacion/editar/nombre/'+str(ubicacion_id),
                headers=headers,
                data=json.dumps(datos)
            )
            if(response.status_code == requests.codes.ok):
                return redirect("ubicacion_mostrar",ubicacion_id=ubicacion_id)
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
                            'ubicacion/actualizar_nombre.html',
                            {"formulario":formulario,"ubicacion":ubicacion})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
    return render(request, 'ubicacion/actualizar_nombre.html',{"formulario":formulario,"ubicacion":ubicacion})

def ubicacion_eliminar(request, ubicacion_id):
    try:
        headers = crear_cabecera()
        response = requests.delete(
            'http://127.0.0.1:8000/api/v1/ubicacion/eliminar/'+str(ubicacion_id),
            headers=headers,
        )
        if(response.status_code == requests.codes.ok):
            return redirect("ubicacion")
        else:
            print(response.status_code)
            response.raise_for_status()
    except Exception as err:
        print(f'Ocurrió un error: {err}')
        return mi_error_500(request)
    return redirect('ubicacion')


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

def perfil_publico_obtener(request, perfil_publico_id):
    perfil_publico = helper.obtener_perfil_publico(perfil_publico_id)
    return render (request, 'perfil_publico/perfil_publico.html',{"perfil_publico":perfil_publico})


def crear_perfil_publico(request):
    if (request.method == "POST"):
        try:
            formulario = PerfilPublicoForm(request.POST)
            headers = {"Content-Type":"application/json"}
            
            datos = formulario.data

            
            response = requests.post(
                'http://127.0.0.1:8000/api/v1/perfil_publico/crear',
                headers=headers,
                data=json.dumps(datos)
            )
            if(response.status_code == requests.codes.ok):
                return redirect("perfil_publico")
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
                            'perfil_publico/crear.html',
                            {"formulario":formulario})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
        
    else:
         formulario = PerfilPublicoForm(None)
    return render(request, 'perfil_publico/crear.html',{"formulario":formulario})


def perfil_publico_editar(request, perfil_publico_id):
    
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    perfil_publico = helper.obtener_perfil_publico(perfil_publico_id)
    formulario = PerfilPublicoForm(datosFormulario,
                        initial={
                            'id':perfil_publico['id'],
                            'descripcion':perfil_publico['descripcion'],
                            'deportes_fav':perfil_publico['deportes_fav'],
                            'hitos_publicos':perfil_publico["hitos_publicos"],
                            'lugar_fav':perfil_publico['lugar_fav'], 
                            'usuarios':perfil_publico['usuarios'], 
                        })
    if (request.method == "POST"):
        try:
            formulario = PerfilPublicoForm(request.POST)
            headers = {"Content-Type":"application/json"}
            datos = request.POST.copy()
            
            response = requests.put(
                'http://127.0.0.1:8000/api/v1/perfil_publico/editar/'+str(perfil_publico_id),
                headers=headers,
                data=json.dumps(datos)
            )
            if(response.status_code == requests.codes.ok):
                return redirect("perfil_publico_obtener",perfil_publico_id=perfil_publico_id)
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
                            'perfil_publico/actualizar.html',
                            {"formulario":formulario,"perfil_publico":perfil_publico})
            else:
                return mi_error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return mi_error_500(request)
    return render(request, 'perfil_publico/actualizar.html',{"formulario":formulario,"perfil_publico":perfil_publico})


def perfil_publico_eliminar(request, perfil_publico_id):
    try:
        headers = crear_cabecera()
        response = requests.delete(
            'http://127.0.0.1:8000/api/v1/perfil_publico/eliminar/'+str(perfil_publico_id),
            headers=headers,
        )
        if(response.status_code == requests.codes.ok):
            return redirect("perfil_publico")
        else:
            print(response.status_code)
            response.raise_for_status()
    except Exception as err:
        print(f'Ocurrió un error: {err}')
        return mi_error_500(request)
    return redirect('perfil_publico')
    
    
    #Páginas de Error
def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

#Páginas de Error
def mi_error_500(request,exception=None):
    return render(request, 'errores/500.html',None,None,500)