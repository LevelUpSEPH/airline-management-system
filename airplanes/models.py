from django.db import models

class AirplaneModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Airplane(models.Model):
    tail_number = models.CharField(max_length=20, unique=True)
    model = models.ForeignKey(AirplaneModel, on_delete=models.CASCADE, related_name='airplanes')
    capacity = models.PositiveIntegerField()
    production_year = models.PositiveIntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.tail_number