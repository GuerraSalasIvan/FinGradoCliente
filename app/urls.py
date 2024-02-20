from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.equipos_lista_api, name='indice'),
    
    #-------------------- EQUIPOS -------------------
    path('equipo/<int:equipo_id>', views.equipo_obtener, name='equipo_obtener'),
    path('equipo/editar/<int:equipo_id>',views.equipo_editar,name='equipo_editar'),
    path('equipo/editar/nombre/<int:equipo_id>',views.equipo_editar_nombre,name='equipo_editar_nombre'),
    path('equipo_busqueda_simple', views.equipo_busqueda_simple, name='equipo_busqueda_simple'),
    path('equipo/buscar_avanzado', views.buscar_avanzado_equipo, name='buscar_avanzado_equipo'),
    path('equipo/crear', views.crear_equipo, name='crear_equipo'),
    path('equipo/eliminar/<int:equipo_id>',views.equipo_eliminar,name='equipo_eliminar'),
    
    #------------------- UBICACION ------------------
    path('ubicacion/<int:ubicacion_id>', views.ubicacion_obtener, name='ubicacion_obtener'),
    
    path('ubicacion/buscar_avanzado', views.buscar_avanzado_ubicacion, name='buscar_avanzado_ubicacion'),
    path('ubicacion/crear', views.crear_ubicacion, name='crear_ubicacion'),
    path('ubicacion/editar/<int:ubicacion_id>',views.ubicacion_editar,name='ubicacion_editar'),
    path('ubicacion/eliminar/<int:ubicacion_id>',views.ubicacion_eliminar,name='ubicacion_eliminar'),
    path('ubicacion', views.ubicacion_lista_api, name='ubicacion'),
    
    #----------------- PERFIL PUBLICO ---------------
    path('perfil_publico/<int:perfil_publico_id>', views.perfil_publico_obtener, name='perfil_publico_obtener'),
    
    path('perfil_publico/buscar_avanzado', views.buscar_avanzado_perfil_publico, name='buscar_avanzado_perfil_publico'),
    path('perfil_publico/eliminar/<int:perfil_publico_id>',views.perfil_publico_eliminar,name='perfil_publico_eliminar'),
    path('perfil_publico/crear', views.crear_perfil_publico, name='crear_perfil_publico'),
    path('perfil_publico/editar/<int:perfil_publico_id>',views.perfil_publico_editar,name='perfil_publico_editar'),
    path('perfil_publico', views.perfil_publico_lista_api, name='perfil_publico'),
    
    #----------------- SESION ---------------
    path('registrar',views.registrar_usuario,name='registrar_usuario'),
    #path('login',views.login,name='login'),
    #path('logout',views.logout,name='logout'),
    
    
    
]