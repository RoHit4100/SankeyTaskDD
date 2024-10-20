from django.urls import path
from . import views

urlpatterns = [
    path('addtrip/', views.addTrip, name='addTrip'),
]
