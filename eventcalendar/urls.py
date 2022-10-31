from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('<int:year>/<str:month>', views.show_html, name='show_html'),
    path('create-event/', views.create_event, name='create-event'),
    path('events/', views.all_events, name='all_events')
]
