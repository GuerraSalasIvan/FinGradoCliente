from django import forms
from django.forms import ModelForm
from .models import *
from datetime import date
import datetime
from .helper import *

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
            
            deportesDisponibles = helper.obtener_deportes_select()
            self.fields["deporte"] = forms.ChoiceField(
                choices=deportesDisponibles,
                widget=forms.Select,
                required=True,
            )
            
            ligaDisponibles = helper.obtener_ligas_select()
            print(ligaDisponibles)
            self.fields["liga"] = forms.ChoiceField(
                choices=ligaDisponibles,
                widget=forms.Select,
                required=True,
            )
            
            
            
            
