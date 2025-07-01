from django.db import models
from location.models import Location


class Flight(models.Model):
    flight_number = models.CharField(max_length = 100, unique=True)
    departure = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='arrivals')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airplane = models.ForeignKey('airplanes.Airplane', on_delete=models.CASCADE, related_name='flights')