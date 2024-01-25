from django import forms
from django.forms import ModelForm
from .models import *
from datetime import date
import datetime

class BusquedaequipoForm(forms.Form):
    textoBusqueda = forms.CharField(required=True)