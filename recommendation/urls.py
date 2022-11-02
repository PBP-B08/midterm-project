from django.urls import path
from recommendation.views import index, addProvince, addArea, show_json, delete_province, detail, show_area_json, delete_area, detail_area

app_name = 'recommendation'

urlpatterns = [
    path('', index, name='index'),
    path('addProvince/', addProvince, name='addProvince'),
    path('json/', show_json, name='show_json'),
    path('deleteProvince/<int:pk>/', delete_province, name='delete_province'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('detail/<int:pk>/addArea/', addArea, name='addArea'),
    path('detail/<int:pk>/json/', show_area_json, name='show_area_json'),
    path('detail/<int:pk>/deleteArea/<int:area_pk>/',
         delete_area, name='delete_area'),
    path('detail/<int:pk>/detailArea/<int:area_pk>/',
         detail_area, name='detail_area'),
]
