import imp
from turtle import title
from django import forms
from .models import Province, Area


# class RecommendationForm(forms.ModelForm):
#     class Meta:
#         model = Recommendation
#         fields = ['title', 'image', 'description', 'summary']


class ProvinceForm(forms.ModelForm):
    title = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Province title'}))
    header = forms.CharField(max_length=500, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter a brief header'}))
    summary = forms.CharField(max_length=500, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter a brief summary'}))

    class Meta:
        model = Province
        fields = ['title', 'header', 'summary']


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['title', 'province', 'summary', 'description']
