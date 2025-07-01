from django.urls import path
from .views import (
    AirplaneModelListCreateAPIView,
    AirplaneModelRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('airplanemodels/', AirplaneModelListCreateAPIView.as_view(), name='airplanemodel-list-create'),
    path('airplanemodels/<int:pk>/', AirplaneModelRetrieveUpdateDestroyAPIView.as_view(), name='airplanemodel-detail'),
]