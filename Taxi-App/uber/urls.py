from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('', views.ride_list, name='ride_list'),
    # path('post/<int:pk>/', views.ride_detail, name='ride_detail'),
    path('ride/produce', views.produce_rides, name='produce_ride'),
    path('ride/visualize', views.visualize, name='visualize_ride'),
    # path('ride/consume', views.consume_rides, name="consume_ride"),
]
