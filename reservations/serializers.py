from rest_framework import serializers
from .models import Reservation
from flights.serializers import FlightSerializer
from users.serializers import PassengerSerializer
from users.models import Passenger
from flights.models import Flight
from .validators import AirplaneCapacityValidator
from .utilities import send_reservation_email

class ReservationSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(read_only=True)
    flight = FlightSerializer(read_only=True)

    passenger_id = serializers.PrimaryKeyRelatedField(
        source='passenger',
        queryset=Passenger.objects.all(),
        write_only=True
    )
    flight_id = serializers.PrimaryKeyRelatedField(
        source='flight',
        queryset=Flight.objects.all(),
        write_only=True
    )

    class Meta:
        model = Reservation
        fields = ['id', 'passenger', 'passenger_id', 'flight', 'flight_id', 'reservation_code', 'status', 'created_at']
        read_only_fields = ['id', 'reservation_code', 'created_at']

    def validate(self, attrs):
        flight = attrs['flight']
        AirplaneCapacityValidator()(flight)
        return attrs

    def create(self, validated_data):
        reservation = super().create(validated_data)
        send_reservation_email(reservation.passenger.email, reservation.reservation_code)
        return reservation