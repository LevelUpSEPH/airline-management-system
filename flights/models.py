from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Flight(models.Model):
    flight_number = models.CharField(max_length = 100, unique=True)
    departure = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='arrivals')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airplane = models.ForeignKey('airplanes.Airplane', on_delete=models.CASCADE, related_name='flights')