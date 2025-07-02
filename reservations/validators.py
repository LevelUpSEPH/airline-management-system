from rest_framework.exceptions import ValidationError
from airplanes.models import Airplane
from flights.models import Flight

class AirplaneCapacityValidator:
    def __call__(self, flight):
        reserved_count = flight.reservations.count()
        capacity = flight.airplane.capacity
        if reserved_count >= capacity:
            raise ValidationError("This flight is fully booked.")
