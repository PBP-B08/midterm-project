from dataclasses import fields

from django import forms
from django.forms import ModelForm
from PlanYourTrip.models import PlanProperties
#pilihan = [('1', 'First'), ('2', 'Second')]
class InputForm(forms.ModelForm):
    
    class Meta:
        model = PlanProperties
        fields = [
            'destinasi',
            'aktivitas',
            'lokasi',
        ]

    # destination = forms.ChoiceField(widget=forms.SelectMultiple, choices=pilihan)
    # date = forms.DateField()
