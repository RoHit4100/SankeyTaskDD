from django.db import models

class Route(models.Model):
    route_id = models.CharField(max_length=10, primary_key=True, unique=True)  # primary key
    user_id = models.CharField(max_length=50)
    route_name = models.CharField(max_length=255)
    route_origin = models.CharField(max_length=255)
    route_destination = models.CharField(max_length=255)
    route_stops = models.JSONField()  # Storing list of stops as JSON

    def __str__(self):
        return self.route_id
