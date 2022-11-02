from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_calendar, name='show_html'),
    path('create-event/', views.create_event, name='create-event'),
    path('json/', views.event_data_json, name='json')
]
