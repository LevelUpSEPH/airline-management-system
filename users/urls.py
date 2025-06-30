from django.urls import path
from .views import PassengerListCreateAPIView, PassengerRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('passengers/', PassengerListCreateAPIView.as_view(), name = 'passenger-list-create'),
    path('passengers/<int:id>/', PassengerRetrieveUpdateDestroyAPIView.as_view, name='passenger-detail')    
]