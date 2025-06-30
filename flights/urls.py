from django.urls import path
from .views import (
    FlightListCreateAPIView,
    FlightRetrieveUpdateDestroyAPIView,
    FlightReservationsAPIView,
    LocationListCreateAPIView,
    LocationRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('flights/', FlightListCreateAPIView.as_view()),
    path('flights/<int:id>/', FlightRetrieveUpdateDestroyAPIView.as_view()),
    path('flights/<int:id>/reservations/', FlightReservationsAPIView.as_view()),
    path('locations/', LocationListCreateAPIView.as_view(), name='location-list-create'),
    path('locations/<int:id>/', LocationRetrieveUpdateDestroyAPIView.as_view(), name='location-detail'),
]