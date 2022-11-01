from django.urls import path
from faq_review.views import show_faq_review, add_review, show_json_faq, show_json_review, show_username

app_name = 'faq_review'

urlpatterns = [
        path('', show_faq_review, name='show_faq_review'),
        path('add/', add_review, name='add_review'),
        path('show_json_faq/', show_json_faq, name='show_json_faq'),
        path('show_json_review/', show_json_review, name='show_json_review'),
        path('show_username/', show_username, name='show_username'),
]