from django.forms import ModelForm
from customer.models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        # fields = "__all__"
        exclude = ["primary_phone",]

class BuyNumberForm(ModelForm):
    class Meta:
        model = CustomerNumber
        fields = ['phone_number','is_primary']
        # fields = "__all__"
