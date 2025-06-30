from rest_framework import serializers
from .models import Reservation
from flights.serializers import FlightSerializer
from users.serializers import PassengerSerializer

class ReservationSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(read_only=True)
    flight = FlightSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = ['id', 'passenger', 'flight', 'reservation_code', 'status', 'created_at']
        read_only = ['id', 'reservation_code', 'created_at']