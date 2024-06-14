from django.urls import path
from . import views
 
urlpatterns = [
    path('get_drf_ip/', views.get_drf_ip, name='get_drf_ip'),
    path('', views.index, name='index'),
]
