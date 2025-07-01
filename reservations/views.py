from django.shortcuts import render
from .models import Reservation
from rest_framework import generics
from .serializers import ReservationSerializer

class ReservationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer