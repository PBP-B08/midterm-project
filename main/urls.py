from django.urls import include, path
from main.views import index, login_user, register, logout_user

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
]
