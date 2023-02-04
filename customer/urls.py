from django.urls import path
from .views import *
urlpatterns = [
    path('',registerCustomer,name='register'),
    path('add_number/<int:id>/',addNumber,name='add_number'),
]