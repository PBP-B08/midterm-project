from django.urls import path
from faq_review.views import show_faq, show_review, add_review, show_json_faq, show_json_review, delete_review

app_name = 'faq-review'

urlpatterns = [
        path('', show_faq, name='show_faq'),
        path('review/', show_review, name='show_review'),
        path('add/', add_review, name='add_review'),
        path('delete/<int:pk>/', delete_review, name='delete_review'),
        path('show_json_faq/', show_json_faq, name='show_json_faq'),
        path('show_json_review/', show_json_review, name='show_json_review'),
]