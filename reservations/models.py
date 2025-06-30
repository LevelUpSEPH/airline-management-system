import uuid
from django.db import models
from django.utils import timezone

class Reservation(models.Model):
    passenger = models.ForeignKey("users.Passenger", on_delete=models.CASCADE, related_name='reservations')
    flight = models.ForeignKey("flights.Flight", on_delete=models.CASCADE, related_name='reservations')
    reservation_code = models.CharField(max_length=12, unique=True, editable=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.reservation_code:
            self.reservation_code = uuid.uuid4().hex[:12].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.reservation_code
