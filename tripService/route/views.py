from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Route
from .serializers import RouteSerializer

@api_view(['POST'])
def addRoute(request):
    try:
        if request.method == 'POST':
            print(request.data)
            # Pass request data to serializer
            serializer = RouteSerializer(data=request.data)
            
            # Validate the data
            print(serializer.is_valid())
            if serializer.is_valid():
                # Save the validated data to the database
                serializer.save()
                return Response({"message": "Route successfully created"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
