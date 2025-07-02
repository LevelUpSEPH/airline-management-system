# flights/validators.py
from datetime import timedelta
from rest_framework.exceptions import ValidationError
from .models import Flight

def validate_flight_conflicts(airplane, departure_time, arrival_time, exclude_flight_id=None):
    if arrival_time <= departure_time:
        raise ValidationError("Arrival time must be after departure time.")

    buffer = timedelta(hours=1)

    conflicts = Flight.objects.filter(airplane=airplane).exclude(id=exclude_flight_id)

    for flight in conflicts:
        if (
            flight.departure_time - buffer < arrival_time and
            flight.arrival_time + buffer > departure_time
        ):
            raise ValidationError(
                f"Conflict with flight {flight.flight_number}. Airplane must have 1 hour between flights."
            )
