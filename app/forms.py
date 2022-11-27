from django import forms
from .models import BotasCarrito

class BotasCarritoForm(forms.ModelForm):
    class Meta:
        model = BotasCarrito
        fields = '__all__'