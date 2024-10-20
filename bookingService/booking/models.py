import re
from django.db import models
from django.core.validators import MinValueValidator


class Booking(models.Model):
    ticket_id = models.CharField(max_length=10, primary_key=True)
    trip_id = models.CharField(max_length=10)
    traveler_name = models.CharField(max_length=50)
    traveler_number = models.CharField(max_length=15)
    traveler_email = models.EmailField(max_length=254)
    ticket_cost = models.IntegerField(validators=[MinValueValidator(0)])  # non-negative cost

    def __str__(self):
        return self.ticket_id
