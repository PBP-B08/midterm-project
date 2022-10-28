import imp
from django import forms
from .models import Recommendation, Province, Area


class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ['title', 'image', 'description', 'summary']


class ProvinceForm(forms.ModelForm):
    class Meta:
        model = Province
        fields = ['name', 'header', 'summary']


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'province', 'summary', 'description']
