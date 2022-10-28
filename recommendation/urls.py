from django.urls import path
from recommendation.views import index, createRecommendation, detail

app_name = 'recommendation'

urlpatterns = [
    path('', index, name='index'),
    path('createRecommendation/', createRecommendation,
         name='createRecommendation'),
    path('detail/<int:recommendation_id>/', detail, name='detail'),
    # path('login/', login_user, name='login'),
    # path('register/', register, name='register'),
    # path('logout/', logout_user, name='logout'),
]
