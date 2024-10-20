from rest_framework import serializers
from .models import Route
import re

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['route_id', 'user_id', 'route_name', 'route_origin', 'route_destination', 'route_stops']

    def validate_route_id(self, value):
        if not re.match(r'^RT\d{8}$', value):
            raise serializers.ValidationError('Route Id must start with (RT) followed by 8 digits.')
        return value
