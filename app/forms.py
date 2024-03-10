from django import forms
from django.forms import ModelForm
from .models import *
from datetime import date
import datetime
from .helper import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BusquedaequipoForm(forms.Form):
    textoBusqueda = forms.CharField(required=True)
    
class BusquedaAvanzadaEquipoForm(forms.Form):
            
    #Obtenemos los campos
    textoBusqueda = forms.CharField(required=False)
    capacidad = forms.IntegerField(required=False)
    
    
class BusquedaAvanzadaUbicacionForm(forms.Form):
            
    #Obtenemos los campos
    textoBusqueda = forms.CharField(required=False)
    capacidad = forms.IntegerField(required=False)
    calle = forms.CharField(required=False)
    
    
class BusquedaAvanzadaPerfil_PublicoForm(forms.Form):
            
    #Obtenemos los campos
    textoBusqueda = forms.CharField(required=False)
    
    '''
    
    
    def __init__(self, *args, **kwargs):
        
        super(BusquedaAvanzadaPerfil_PublicoForm, self).__init__(*args, **kwargs)
        
        lugares = helper.obtener_lugares_select()
        self.fields['lugar'] = forms.ChoiceField(
            choices=lugares,
            widget=forms.Select,
            required=True,
        )
    '''
    
class EquipoForm(forms.Form):
    
        nombre  = forms.CharField(label="Nombre del equipo",
                                  required=True,
                                  max_length=100)
        
        capacidad = forms.IntegerField(label="Capacidad")
        
        def __init__(self, *args, **kwargs):
            super(EquipoForm, self).__init__(*args, **kwargs)
            
            usauriosDisponibles = helper.obtener_usuarios_select()
            self.fields["usuarios"] = forms.ChoiceField(
                choices=usauriosDisponibles,
                widget=forms.SelectMultiple,
                required=True,
            )
            
            deportesDisponibles = helper.obtener_deportes_select()
            self.fields["deporte"] = forms.ChoiceField(
                choices=deportesDisponibles,
                widget=forms.Select,
                required=True,
            )
            
            ligaDisponibles = helper.obtener_ligas_select()
            self.fields["liga"] = forms.ChoiceField(
                choices=ligaDisponibles,
                widget=forms.Select,
                required=True,
            )
            
            coloresDisponibles1 = helper.obtener_colores_select()
            self.fields["color_eq_1"] = forms.ChoiceField(
                choices=coloresDisponibles1,
                widget=forms.Select,
                required=True,
            )
            
            coloresDisponibles2 = helper.obtener_colores_select()
            self.fields["color_eq_2"] = forms.ChoiceField(
                choices=coloresDisponibles2,
                widget=forms.Select,
                required=True,
            )
            
            
            
class UbicacionForm(forms.Form):
    
        nombre  = forms.CharField(label="Nombre Ubicacion",
                                  required=True,
                                  max_length=100)
        
        capacidad = forms.IntegerField(label="Capacidad")
        
        calle  = forms.CharField(label="Nombre de la calle",
                                  required=True,
                                  max_length=150)
        
        def __init__(self, *args, **kwargs):
            super(UbicacionForm, self).__init__(*args, **kwargs)
            
            deportesDisponibles = helper.obtener_deportes_select()
            self.fields["deporte"] = forms.ChoiceField(
                choices=deportesDisponibles,
                widget=forms.Select,
                required=True,
            )
            
            equipoDisponibles = helper.obtener_equipos_select()
            self.fields["equipo"] = forms.ChoiceField(
                choices=equipoDisponibles,
                widget=forms.Select,
                required=False,
            )
            
class PerfilPublicoForm(forms.Form):
    
        descripcion  = forms.CharField(label="descripcion",
                                  required=True,
                                  max_length=100)
        
        hitos_publicos  = forms.CharField(label="hitos publicos",
                                  required=True,
                                  max_length=100)

        
        deportes_fav  = forms.CharField(label="deporte favorito",
                                  required=True,
                                  max_length=150)
        
        def __init__(self, *args, **kwargs):
            super(PerfilPublicoForm, self).__init__(*args, **kwargs)
            
            lugaresDisponibles = helper.obtener_lugares_select()
            self.fields["lugar_fav"] = forms.ChoiceField(
                choices=lugaresDisponibles,
                widget=forms.Select,
                required=True,
            )
            
            usauriosDisponibles = helper.obtener_usuarios_select()
            self.fields["usuarios"] = forms.ChoiceField(
                choices=usauriosDisponibles,
                widget=forms.Select,
                required=True,
            )
            
            
class PartidoForm(forms.Form):
    
        fecha  = forms.DateTimeField(
                                    label='Fecha y Hora del Partido',
                                    widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
                                    input_formats=['%Y-%m-%dT%H:%M'])
        
        puntos_local = forms.IntegerField(label="Puntos Local")
        
        puntos_visitante = forms.IntegerField(label="Puntos Visitante")
        
        color_local = forms.CharField(label='Color local',
                                      initial=2,
                                      widget=forms.HiddenInput(),
                                      required=False)
        
        color_visitante = forms.CharField(label='Color Visitante',
                                      initial=1,
                                      widget=forms.HiddenInput(),
                                      required=False)
               
        def __init__(self, *args, **kwargs):
            super(PartidoForm, self).__init__(*args, **kwargs)

            
            ubicacionDisponibles = helper.obtener_lugares_select()
            self.fields["ubicacion"] = forms.ChoiceField(
                choices=ubicacionDisponibles,
                widget=forms.Select,
                required=True,
            )
            
            equipoLocalDisponibles = helper.obtener_equipos_select()
            self.fields["equipo_local"] = forms.ChoiceField(
                choices=equipoLocalDisponibles,
                widget=forms.Select,
                required=False,
            )
            
            equipoVisitanteDisponibles = helper.obtener_equipos_select()
            self.fields["equipo_visitante"] = forms.ChoiceField(
                choices=equipoVisitanteDisponibles,
                widget=forms.Select,
                required=False,
            )
            
            
            
class EquipoActualizarNombreForm(forms.Form):
    nombre = forms.CharField(label="Nombre del Equipo",
                             required=True, 
                             max_length=100,
                             help_text="100 caracteres como máximo")
    
class UbicacionActualizarNombreForm(forms.Form):
    nombre = forms.CharField(label="Nombre del Pabellon",
                             required=True, 
                             max_length=200,
                             help_text="200 caracteres como máximo")
    
class RegistroForm(UserCreationForm): 
    roles = (
                                (2, 'jugador'),
                                (3, 'entrenador'),
                            )   
    generos = (
        ('MAS','Masculino'),
        ('FEM','Femenino'),
        ('---','Sin_Asignar'),
    )
        
    
    
    rol = forms.ChoiceField(choices=roles) 
    
    edad = forms.IntegerField(required=True)
    
    sexo = forms.ChoiceField(choices=generos)
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','rol', 'edad', 'sexo')
        
class LoginForm(forms.Form):
    usuario = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

            
            
