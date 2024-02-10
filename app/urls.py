from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.equipos_lista_api, name='indice'),
    
    #-------------------- EQUIPOS -------------------
    path('equipo/<int:equipo_id>', views.equipo_obtener, name='equipo_obtener'),
    path('equipo/editar/<int:equipo_id>',views.equipo_editar,name='equipo_editar'),
    path('equipo_busqueda_simple', views.equipo_busqueda_simple, name='equipo_busqueda_simple'),
    path('equipo/buscar_avanzado', views.buscar_avanzado_equipo, name='buscar_avanzado_equipo'),
    path('equipo/crear', views.crear_equipo, name='crear_equipo'),
    path('equipo/eliminar/<int:equipo_id>',views.equipo_eliminar,name='equipo_eliminar'),
    
    #------------------- UBICACION ------------------
    path('ubicacion/buscar_avanzado', views.buscar_avanzado_ubicacion, name='buscar_avanzado_ubicacion'),
    
    #----------------- PERFIL PUBLICO ---------------
    path('perfil_publico/buscar_avanzado', views.buscar_avanzado_perfil_publico, name='buscar_avanzado_perfil_publico'),
    
]