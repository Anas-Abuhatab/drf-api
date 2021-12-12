from django.urls import path
from .views import Carlist, CarDetail


urlpatterns = [
    path('', Carlist.as_view(), name= 'car_list'),
    path('<int:pk>/', CarDetail.as_view(), name='car_details'),
]