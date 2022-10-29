from django.urls import path
from faq_review.views import show_faq_review, add_review, show_json

app_name = 'faq_review'

urlpatterns = [
        path('faq/', show_faq_review, name='show_faq_review'),
        path('add/', add_review, name='add_review'),
        path('show_json/', show_json, name='show_json'),
]