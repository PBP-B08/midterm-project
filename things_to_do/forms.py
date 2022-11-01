from django import forms
from django.forms import ModelForm
from .models import Food, Event

class FoodForm(ModelForm):
    prov_id = forms.IntegerField(widget=forms.HiddenInput(attrs={'id':'fprov_id', 'Placeholder':'Date'}))
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'id':'fname', 'placeholder': 'Name', 'class':'bg-violet-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':30, 'id':'fdescription', 'placeholder': 'Description', 'class':'bg-violet-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}))
    image = forms.URLField(max_length=255, widget=forms.TextInput(attrs={'id':'fimage', 'placeholder': 'Image URL', 'class':'bg-violet-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}))
    class Meta:
        model = Food
        fields = ['province', 'name', 'description', 'image']   


class EventForm(ModelForm):
    prov_id = forms.IntegerField(widget=forms.HiddenInput(attrs={'id':'eprov_id', 'Placeholder':'Date'}))
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'id':'ename', 'placeholder': 'Name', 'class':'bg-violet-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}))
    # date = forms.DateField(widget=forms.DateInput(attrs={'id':'edate', 'placeholder': 'Date', 'class':'bg-violet-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}))
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'id':'edate', 'placeholder': 'Date', 'class':'bg-violet-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            'type':'date'
        }))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':30, 'id':'edescription', 'placeholder': 'Description', 'class':'bg-violet-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}))
    image = forms.URLField(max_length=255, widget=forms.TextInput(attrs={'id':'eimage', 'placeholder': 'Image URL', 'class':'bg-violet-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}))
    class Meta:
        model = Event
        fields = ['province', 'name', 'date', 'description', 'image']   