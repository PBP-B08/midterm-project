from django.urls import path
from PlanYourTrip.views import *

urlpatterns = [
    path('welcome/', say_helo, name=" "),
    path('helo/', say_form, name="helo"),
    path('show_json', show_json, name="show_json"),
    #path('add/', say_helo, name='add'),
]