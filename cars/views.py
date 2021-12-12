from django.shortcuts import render
from rest_framework import generics
from .serialzers import CarSerialzer
from .models import Car


class Carlist(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerialzer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerialzer