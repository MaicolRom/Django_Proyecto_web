from http.cookies import BaseCookie
from django import forms
from .models import Persona
from crispy_forms.helper import FormHelper

class personaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre', 'cedula', 'archivo')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
