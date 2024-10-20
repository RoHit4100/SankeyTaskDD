from rest_framework import serializers
import re
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        depth = 1
        
    def validate_trip_id(self, value):  # Corrected method name
        if not re.match(r'^TP\d{8}$', value):
            raise serializers.ValidationError('Trip Id must start with (TP) and should be followed by 8 digits.')
        return value
    