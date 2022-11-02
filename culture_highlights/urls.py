from django.urls import path
from . import views

app_name = 'culture_highlights'

urlpatterns = [
    path('highlights/', views.culture_highlights_page, name='highlights'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]