from django.db import models
from route.models import Route

class Trip(models.Model):
    trip_id = models.CharField(primary_key=True, max_length=10)
    user_id = models.CharField(max_length=50)
    vehicle_id = models.CharField(max_length=255)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='trips')  # Use 'trips' for reverse relationship
    driver_name = models.CharField(max_length=255)

    def __str__(self):  
        return self.trip_id
