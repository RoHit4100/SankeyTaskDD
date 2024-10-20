from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import re
from django.core.exceptions import ValidationError
from .models import Booking


# traveler number
def validate_number(value):
    if not re.match(r'^\+?[1-9]\d{1,14}$', value):
        return False
    return True

# ticket_id format
def validate_ticket_id(value):
    if not re.match(r'^TK\d{8}$', value):
        return False
    return True

# trip_id format
def validate_trip_id(value):
    if not re.match(r'^TP\d{8}$', value):
        return False
    return True


# Create your views here.
@csrf_exempt
def addBooking(request):
    try: 
        if request.method == 'POST':
            # First get the data 
            data = json.loads(request.body)
            
            ticket_id = data.get('ticket_id')
            trip_id = data.get('trip_id')
            traveler_name = data.get('traveler_name')
            traveler_number = data.get('traveler_number')
            ticket_cost = data.get('ticket_cost')
            traveler_email = data.get('traveler_email')
            
            # error for missing values
            if not ticket_id or not trip_id or not traveler_name or not traveler_number or not ticket_cost or not traveler_email:
                return JsonResponse({'error': 'Missing Values'}, status=400)
            
            if not validate_ticket_id(ticket_id):
                return JsonResponse({'error': 'Ticket ID must start with (TK) followed by 8 digits.'}, status=400)
            
            if not validate_trip_id(trip_id):
                return JsonResponse({'error': 'Trip ID must start with (TP) followed by 8 digits.'}, status=400)
            
            if not validate_number(traveler_number):
                return JsonResponse({'error': 'Invalid phone number format.'}, status=400)
            
            # Assuming ticket_cost is validated as an integer
            try:
                ticket_cost = int(ticket_cost)
            except ValueError:
                return JsonResponse({'error': 'Ticket cost must be a valid number.'}, status=400)

            # Create booking
            Booking.objects.create(
                ticket_id=ticket_id, 
                trip_id=trip_id, 
                ticket_cost=ticket_cost,
                traveler_name=traveler_name, 
                traveler_number=traveler_number, 
                traveler_email=traveler_email
            )
            return JsonResponse({'message': 'Booking successfully created', 'ticket_id': ticket_id}, status=200)
        else:
            return JsonResponse({'error': 'Invalid request method. Only POST is allowed.'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def bookingListing(request):
    try: 
        if request.method == 'GET':
            # return all the values present in the booking table
            booking = Booking.objects.all().values()
            return JsonResponse(list(booking), safe=False)
        else:
            return JsonResponse({'error': 'Invalid request method. Only GET is allowed.'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
def bookingDetails(request):
    try: 
        if request.method == 'POST':
            # get the data from the request body
            data = json.loads(request.body)
            # only get the ticket id 
            ticket_id = data.get('ticket_id')
            if not ticket_id or not validate_ticket_id(ticket_id):
                return JsonResponse({'error': 'Something Wrong with Ticket ID'}, status=400)
            
            # get the targeted detail
            detail = Booking.objects.get(ticket_id=ticket_id)
            if not detail: 
                return JsonResponse({'error': 'There are no bookings for this Ticket ID'}, status=404)
            print(detail)
            return JsonResponse({
                'ticket_id': detail.ticket_id, 
                'trip_id':detail.trip_id, 
                'ticket_cost':detail.ticket_cost,
                'traveler_name': detail.traveler_name, 
                'traveler_number':detail.traveler_number, 
                'traveler_email':detail.traveler_email
                })
        else:
            return JsonResponse({'error': 'Invalid request method. Only POST is allowed.'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


# @csrf_exempt
# def bookingDetailsTripId(request):
#     try:
#         if request.method == 'GET':
#             # 