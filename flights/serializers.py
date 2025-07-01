from rest_framework import serializers
from .models import Flight, Location
from airplanes.models import Airplane
from airplanes.serializers import AirplaneSerializer

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']
        read_only_fields = ['id']

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
    
    class Meta:
        model = Flight
        fields = ['id', 'flight_number', 'departure', 'departure_id', 'destination', 'destination_id', 'departure_time', 'arrival_time', 'airplane', 'airplane_id']
        read_only_fields = ['id']
