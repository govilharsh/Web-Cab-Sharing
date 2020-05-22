from django.contrib import admin
from django.urls import path, include
from register.views import homepage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', homepage, name='homepage'),
    path('bookings/', include('bookings.urls')),
]
