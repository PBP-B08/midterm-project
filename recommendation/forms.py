from django import forms
from .models import Province, Area


class ProvinceForm(forms.ModelForm):
    title = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5', 'placeholder': 'Province title', 'id': 'provinceTitle'}))
    header = forms.CharField(max_length=500, widget=forms.TextInput(
        attrs={'class': 'form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5', 'placeholder': 'Enter a brief header', 'id': 'provinceHeader'}))
    summary = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 20, 'class': 'form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5', 'placeholder': 'Enter a brief summary', 'id': 'provinceSummary'}))
    image = forms.URLField(max_length=500, widget=forms.TextInput(
        attrs={'class': 'form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5', 'placeholder': 'Enter URL for an image', 'id': 'provinceImage'}))

    class Meta:
        model = Province
        fields = ['title', 'header', 'summary', 'image']


class AreaForm(forms.ModelForm):
    title = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5', 'placeholder': 'Province title', 'id': 'areaTitle'}))
    description = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={'rows': 5, 'cols': 30, 'class': 'form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5', 'placeholder': 'Enter a brief header', 'id': 'areaDescription'}))
    summary = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 20, 'class': 'form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5', 'placeholder': 'Enter a brief summary', 'id': 'areaSummary'}))
    image = forms.URLField(max_length=500, widget=forms.TextInput(
        attrs={'class': 'form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5', 'placeholder': 'Enter URL for an image', 'id': 'areaImage'}))

    class Meta:
        model = Area
        fields = ['title', 'province', 'summary', 'description', 'image']
