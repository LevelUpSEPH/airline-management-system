from rest_framework import serializers
from .models import Flight
from airplanes.models import Airplane
from location.models import Location
from airplanes.serializers import AirplaneSerializer
from location.serializers import LocationSerializer
from .validators import validate_flight_conflicts

class FlightSerializer(serializers.ModelSerializer):
    departure = LocationSerializer(read_only=True)
    destination = LocationSerializer(read_only=True)
    airplane = AirplaneSerializer(read_only=True)

    departure_id = serializers.PrimaryKeyRelatedField(
        source='departure',
        queryset=Location.objects.all(),
        write_only=True
    )
    destination_id = serializers.PrimaryKeyRelatedField(
        source='destination',
        queryset=Location.objects.all(),
        write_only=True
    )
    airplane_id = serializers.PrimaryKeyRelatedField(
        source='airplane',
        queryset=Airplane.objects.all(),
        write_only=True
    )

    def validate(self, data):
        airplane = data.get("airplane")
        departure_time = data.get("departure_time")
        arrival_time = data.get("arrival_time")

        exclude_id = self.instance.id if self.instance else None
        validate_flight_conflicts(airplane, departure_time, arrival_time, exclude_flight_id=exclude_id)

        return data
    
    class Meta:
        model = Flight
        fields = ['id', 'flight_number', 'departure', 'departure_id', 'destination', 'destination_id', 'departure_time', 'arrival_time', 'airplane', 'airplane_id']
        read_only_fields = ['id']
