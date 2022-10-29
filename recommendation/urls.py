from django.urls import path
from recommendation.views import index, addProvince, addArea, show_json, delete_province, detail

app_name = 'recommendation'

urlpatterns = [
    path('', index, name='index'),
    path('addProvince/', addProvince, name='addProvince'),
    # path('addArea/', addArea, name='addArea'),
    path('json/', show_json, name='show_json'),
    path('deleteProvince/<int:pk>/', delete_province, name='delete_province'),
    path('detail/<int:pk>/', detail, name='detail'),
]
