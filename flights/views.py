from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Flight
from .models import Location
from .serializers import FlightSerializer
from .serializers import LocationSerializer
from reservations.serializers import ReservationSerializer

# Create your views here.

class FlightListCreateAPIView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class FlightRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class FlightReservationsAPIView(APIView):
    def get(self, request, id):
        try:
            flight = Flight.objects.get(pk=id)
        except Flight.DoesNotExist:
            return Response({"detail": "Flight not found."}, status=404)

        reservations = flight.reservations.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data, status=200)

class LocationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer