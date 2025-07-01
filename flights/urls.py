from django.urls import path
from .views import (
    FlightListCreateAPIView,
    FlightRetrieveUpdateDestroyAPIView,
    FlightReservationsAPIView,
    LocationListCreateAPIView,
    LocationRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('flights/', FlightListCreateAPIView.as_view(), name='flight-list-create'),
    path('flights/<int:pk>/', FlightRetrieveUpdateDestroyAPIView.as_view(), name='flight-detail'),
    path('flights/<int:pk>/reservations/', FlightReservationsAPIView.as_view(), name='flight-reservations'),
    path('locations/', LocationListCreateAPIView.as_view(), name='location-list-create'),
    path('locations/<int:pk>/', LocationRetrieveUpdateDestroyAPIView.as_view(), name='location-detail'),
]