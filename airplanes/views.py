from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Airplane
from .serializers import AirplaneSerializer
from flights.serializers import FlightSerializer

class AirplaneListCreateAPIView(generics.ListCreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'model', 'capacity', 'production_year', 'status']
    search_fields = ['tail_number']
    ordering_fields = ['production_year', 'capacity']

class AirplaneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

class AirplaneFlightsAPIView(APIView):
    def get(self, request, pk):
        try:
            airplane = Airplane.objects.get(pk=pk)
        except Airplane.DoesNotExist:
            return Response({"detail": "Airplane not found."}, status=404)
        
        flights = airplane.flights.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data, status=200)