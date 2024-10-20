from django.urls import path
from . import views

urlpatterns = [
    # path('helloworld', views.helloWorld, name='helloWorld')
    path('addroute/', views.addRoute, name='addRoute'),
]

