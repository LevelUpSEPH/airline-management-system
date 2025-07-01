from django.urls import path
from .views import (
    AirplaneListCreateAPIView,
    AirplaneRetrieveUpdateDestroyAPIView,
    AirplaneFlightsAPIView
)

urlpatterns = [
    path('airplanes/', AirplaneListCreateAPIView.as_view(), name='airplane-list-create'),
    path('airplanes/<int:pk>/', AirplaneRetrieveUpdateDestroyAPIView.as_view(), name='airplane-detail'),
    path('airplanes/<int:pk>/flights/', AirplaneFlightsAPIView.as_view(), name='airplane-flights'),
]