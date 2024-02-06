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
        
  