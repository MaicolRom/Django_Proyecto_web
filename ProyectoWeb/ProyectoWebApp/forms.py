from http.cookies import BaseCookie
from django import forms
from .models import Persona

class personaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre', 'cedula', 'archivo')