from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Airplane
from .models import AirplaneModel
from .serializers import AirplaneSerializer
from .serializers import AirplaneModelSerializer
from flights.serializers import FlightSerializer

class AirplaneListCreateAPIView(generics.ListCreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

class AirplaneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

class AirplaneFlightsAPIView(APIView):
    def get(self, request, id):
        try:
            airplane = Airplane.objects.get(pk=id)
        except Airplane.DoesNotExist:
            return Response({"detail": "Airplane not found."}, status=404)
        
        flights = airplane.flights.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data, status=200)

class AirplaneModelListCreateAPIView(generic.ListCreateAPIView):
    queryset = AirplaneModel.objects.all()
    serializer_class = AirplaneModelSerializer

class AirplaneModelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AirplaneModel.objects.all()
    serializer_class = AirplaneModelSerializer