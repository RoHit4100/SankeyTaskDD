from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Trip
from route.models import Route
from .serializers import TripSerializer

@api_view(['POST'])
def addTrip(request):
    # Get the route ID from the request data
    route_id = request.data.get('route')
    try:
        # Fetch the Route object using the route ID
        route = Route.objects.get(route_id=route_id)

        # Create the serializer instance
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()  # Save the Trip object, linking it to the Rout
            data = request.data
            trip = Trip.objects.create(trip_id= data.get('trip_id'), user_id=data.get('user_id'), vehicle_id=data.get('vehicle_id'),
                                       route=route, driver_name=data.get('driver_name'))
            return Response({'message': 'Trip successfully added'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Route.DoesNotExist:
        return Response({'error': 'Route not found'}, status=status.HTTP_404_NOT_FOUND)
