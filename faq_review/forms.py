from unicodedata import name
from django import forms
from faq_review.models import reviewUser

class reviewForm(forms.ModelForm):
    class Meta:
        model = reviewUser
        fields = [
            "title",
            "review",
        ]
    title = forms.CharField(widget=forms.TextInput(attrs={"id": "title", "class": "border-4", "name":"title"}))
    review = forms.CharField(widget=forms.Textarea(attrs={"id": "review", "class": "border-4", "review":"review"}))
