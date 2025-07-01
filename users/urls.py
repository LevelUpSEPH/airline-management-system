from django.urls import path
from .views import PassengerListCreateAPIView, PassengerRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('passengers/', PassengerListCreateAPIView.as_view(), name = 'passenger-list-create'),
    path('passengers/<int:pk>/', PassengerRetrieveUpdateDestroyAPIView.as_view(), name='passenger-detail')    
]