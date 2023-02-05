from django.urls import path
from .views import *
urlpatterns = [
    path("",customer,name='customer'),
    path('register/',registerCustomer,name='register'),
    path('add_number/<str:id>/',addNumber,name='add_number'),
]