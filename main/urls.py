

=======
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from main.views import index, login_user, register, logout_user, profile, update_profile


app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
    path('recommendation/', include('recommendation.urls')),
    path('event-calendar/', include('eventcalendar.urls')),
    # path('things-to-do/', include('things_to_do.urls')),

    path('plan/', include('PlanYourTrip.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)