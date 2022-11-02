from django.urls import path
from PlanYourTrip.views import say_helo, say_plan, say_form

urlpatterns = [
    path('welcome/', say_helo, name=" "),
    path('helo/', say_form, name="helo"),
    #path('add/', say_helo, name='add'),
]