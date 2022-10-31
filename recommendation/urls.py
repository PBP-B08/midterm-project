from django.urls import path
from recommendation.views import index, addProvince, addArea, show_json, delete_province, detail, show_area_json, delete_area

app_name = 'recommendation'

urlpatterns = [
    path('', index, name='index'),
    path('addProvince/', addProvince, name='addProvince'),
    # path('addArea/', addArea, name='addArea'),
    path('json/', show_json, name='show_json'),
    path('deleteProvince/<int:pk>/', delete_province, name='delete_province'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('detail/<int:pk>/addArea/', addArea, name='addArea'),
    # path('addArea/<int:pk>/', addArea, name='addArea'),
    path('detail/<int:pk>/json/', show_area_json, name='show_area_json'),
    path('deleteArea/<int:pk>/', delete_area, name='delete_area'),
]
