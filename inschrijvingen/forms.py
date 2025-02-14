from django import forms
from .models import Inschrijving, Workshop

class InschrijvingForm(forms.ModelForm):
    class Meta:
        model = Inschrijving
        fields = ['naam', 'email' ]  # Zorg ervoor dat workshop in de form staat

   
