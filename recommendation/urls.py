from django.urls import path
from recommendation.views import index, createRecommendation, detail, addProvince, addArea, show_json

app_name = 'recommendation'

urlpatterns = [
    path('', index, name='index'),
    path('createRecommendation/', createRecommendation,
         name='createRecommendation'),
    path('detail/<int:recommendation_id>/', detail, name='detail'),
    path('addProvince/', addProvince, name='addProvince'),
    path('addArea/', addArea, name='addArea'),
    path('json/', show_json, name='show_json'),
    # path('login/', login_user, name='login'),
    # path('register/', register, name='register'),
    # path('logout/', logout_user, name='logout'),
]
