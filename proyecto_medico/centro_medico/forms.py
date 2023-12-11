# centro_medico/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PacienteRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    telefono = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'telefono', 'password1', 'password2']
