from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AirplaneModel
from .serializers import AirplaneModelSerializer

class AirplaneModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = AirplaneModel.objects.all()
    serializer_class = AirplaneModelSerializer

class AirplaneModelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AirplaneModel.objects.all()
    serializer_class = AirplaneModelSerializer