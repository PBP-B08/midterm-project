from django.urls import include, path
from django.conf.urls.static import static

from .views import show_general, show_food_event, json_food, json_event, json_province

app_name = 'things_to_do'

urlpatterns = [
    path('', show_general, name='show'),
    path('<int:prov_id>/', show_food_event, name='show_province'),
    path('json/food/<int:prov_id>/', json_food, name='json_food'),
    path('json/event/<int:prov_id>/', json_event, name='json_event'),
    path('json/province', json_province, name='json_province'),
]