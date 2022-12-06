from django import forms
from .models import BotasCarrito
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BotasCarritoForm(forms.ModelForm):
    class Meta:
        model = BotasCarrito
        fields = '__all__'


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']