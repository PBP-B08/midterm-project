from django import forms
from .models import Province, Area


class ProvinceForm(forms.ModelForm):
    title = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control w-full', 'placeholder': 'Province title', 'id': 'provinceTitle'}))
    header = forms.CharField(max_length=500, widget=forms.TextInput(
        attrs={'class': 'form-control w-full', 'placeholder': 'Enter a brief header', 'id': 'provinceHeader'}))
    summary = forms.CharField(max_length=500, widget=forms.TextInput(
        attrs={'class': 'form-control w-full', 'placeholder': 'Enter a brief summary', 'id': 'provinceSummary'}))
    image = forms.URLField(max_length=500, widget=forms.TextInput(
        attrs={'class': 'form-control w-full', 'placeholder': 'Enter a URL for an image', 'id': 'provinceImage'}))

    class Meta:
        model = Province
        fields = ['title', 'header', 'summary', 'image']


class AreaForm(forms.ModelForm):
    title = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control w-full', 'placeholder': 'Province title', 'id': 'areaTitle'}))
    description = forms.CharField(max_length=500, widget=forms.TextInput(
        attrs={'class': 'form-control w-full', 'placeholder': 'Enter a brief header', 'id': 'areaDescription'}))
    summary = forms.CharField(max_length=500, widget=forms.TextInput(
        attrs={'class': 'form-control w-full', 'placeholder': 'Enter a brief summary', 'id': 'areaSummary'}))
    image = forms.URLField(max_length=500, widget=forms.TextInput(
        attrs={'class': 'form-control w-full', 'placeholder': 'Enter a URL for an image', 'id': 'areaImage'}))

    class Meta:
        model = Area
        fields = ['title', 'province', 'summary', 'description', 'image']
