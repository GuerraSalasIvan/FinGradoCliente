from django import forms
from django.forms import ModelForm
from .models import *
from datetime import date
import datetime

class BusquedaequipoForm(forms.Form):
    textoBusqueda = forms.CharField(required=True)
    
class BusquedaAvanzadaEquipoForm(forms.Form):
            
    #Obtenemos los campos
    textoBusqueda = forms.CharField(required=False)

    capacidad = forms.IntegerField(required=False)
        
  