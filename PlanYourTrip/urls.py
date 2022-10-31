from django.urls import path
from PlanYourTrip.views import say_helo, say_plan, say_form

urlpatterns = [
    path('helo/', say_plan, name='helo'),
    path('add/', say_form, name='add'),
]