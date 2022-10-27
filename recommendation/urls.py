from django.urls import path
from recommendation.views import index

app_name = 'recommendation'

urlpatterns = [
    path('', index, name='index'),
    # path('login/', login_user, name='login'),
    # path('register/', register, name='register'),
    # path('logout/', logout_user, name='logout'),
]
