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
    title = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Area title'}))
    province = forms.ModelChoiceField(queryset=Province.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control', 'placeholder': 'Select a province'}))
    summary = forms.CharField(max_length=500, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter a brief summary'}))
    description = forms.CharField(max_length=1000, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter a brief description'}))

    class Meta:
        model = Area
        fields = ['title', 'province', 'summary', 'description']
