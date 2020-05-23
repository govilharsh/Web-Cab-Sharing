from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'register'


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('logged_out/', auth_views.LogoutView.as_view(), name='user_logout'),
]
