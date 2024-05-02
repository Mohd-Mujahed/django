# models.py
from django.db import models

class PickupSchedule(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.pickup_date} {self.pickup_time}"
