from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.ride_list, name='ride_list'),
    path('post/<int:pk>/', views.ride_detail, name='ride_detail'),
]
