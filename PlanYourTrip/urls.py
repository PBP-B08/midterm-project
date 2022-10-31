from django.urls import path
from PlanYourTrip.views import say_helo

urlpatterns = [
    path('helo/', say_helo, name='helo'),
]