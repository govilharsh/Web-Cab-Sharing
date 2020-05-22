from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<booking_id>/', views.DetailView.as_view(), name='detail')
]
