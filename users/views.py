from django.shortcuts import render
from rest_framework import generics
from .models import Passenger
from .serializers import PassengerSerializer

class PassengerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class PassengerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer