from django.urls import include, path

from .views import delete_event, show_general, show_food_event, json_food, json_event, json_province
from .views import add_event, add_food, update_event, update_food, delete_event, delete_food

app_name = 'things_to_do'

urlpatterns = [
    path('', show_general, name='show'),
    path('<int:prov_id>/', show_food_event, name='show_province'),
    path('json/food/<int:prov_id>/', json_food, name='json_food'),
    path('json/event/<int:prov_id>/', json_event, name='json_event'),
    path('json/province', json_province, name='json_province'),
    path('add/event', add_event, name='add_event'),
    path('add/food', add_food, name='add_food'),
    path('update/event/<int:event_id>', update_event, name='update_event'),
    path('update/food/<int:food_id>', update_food, name='update_food'),
    path('delete/event/<int:event_id>', delete_event, name='delete_event'),
    path('delete/food/<int:food_id>', delete_food, name='delete_food'),
]