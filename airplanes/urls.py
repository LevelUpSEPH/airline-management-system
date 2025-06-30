from django.urls import path
from .views import (
    AirplaneListCreateAPIView,
    AirplaneRetrieveUpdateDestroyAPIView,
    AirplaneFlightsAPIView,
    AirplaneModelListCreateAPIView,
    AirplaneModelRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('airplanes/', AirplaneListCreateAPIView.as_view()),
    path('airplanes/<int:id>/', AirplaneRetrieveUpdateDestroyAPIView.as_view()),
    path('airplanes/<int:id>/flights/', AirplaneFlightsAPIView.as_view()),
    path('airplanemodels/', AirplaneModelListCreateAPIView.as_view(), name='airplanemodel-list-create'),
    path('airplanemodels/<int:id>/', AirplaneModelRetrieveUpdateDestroyAPIView.as_view(), name='airplanemodel-detail'),
]