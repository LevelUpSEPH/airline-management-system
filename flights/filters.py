import django_filters
from .models import Flight

class FlightFilter(django_filters.FilterSet):
    departure_time = django_filters.DateTimeFromToRangeFilter()
    arrival_time = django_filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Flight
        fields = ['departure_id', 'destination_id', 'departure_time', 'arrival_time']
