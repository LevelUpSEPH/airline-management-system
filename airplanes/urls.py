from django.urls import path
from .views import (
    AirplaneListCreateAPIView,
    AirplaneRetrieveUpdateDestroyAPIView,
    AirplaneFlightsAPIView,
    AirplaneModelListCreateAPIView,
    AirplaneModelRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('airplanes/', AirplaneListCreateAPIView.as_view(), name='airplane-list-create'),
    path('airplanes/<int:pk>/', AirplaneRetrieveUpdateDestroyAPIView.as_view(), name='airplane-detail'),
    path('airplanes/<int:pk>/flights/', AirplaneFlightsAPIView.as_view(), name='airplane-flights'),
    path('airplanemodels/', AirplaneModelListCreateAPIView.as_view(), name='airplanemodel-list-create'),
    path('airplanemodels/<int:pk>/', AirplaneModelRetrieveUpdateDestroyAPIView.as_view(), name='airplanemodel-detail'),
]