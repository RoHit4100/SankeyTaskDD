from django.urls import path
from . import views

urlpatterns = [
    path('addbooking/', views.addBooking, name='addBooking'),
    path('bookinglist/', views.bookingListing, name='bookingListing'),
    path('bookingdetails/', views.bookingDetails, name='bookingDetails')
]
