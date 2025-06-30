from django.urls import path
from .views import ReservationListCreateAPIView, ReservationRetrieveUpdateAPIView

urlpatterns = [
    path('reservations/', ReservationListCreateAPIView.as_view(), name='reservation-list-create'),
    path('reservations/<int:id>/', ReservationRetrieveUpdateAPIView.as_view(), name='reservation-detail-update'),
]