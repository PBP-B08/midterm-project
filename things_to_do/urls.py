from django.urls import include, path
from django.conf.urls.static import static

from .views import show_food_event, json_food, json_event

app_name = 'things_to_do'

urlpatterns = [
    # path('', show_general, name='show'),
    path('<int:prov_id>/', show_food_event, name='show'),
    path('json/food/<int:prov_id>/', json_food, name='json_food'),
    path('json/event/<int:prov_id>/', json_event, name='json_event'),
]