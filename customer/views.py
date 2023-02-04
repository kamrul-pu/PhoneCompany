from django.shortcuts import render,redirect
from .forms import CustomerForm,BuyNumberForm
from .models import *
# Create your views here.

def registerCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            phone_numbers = PhoneNumber.objects.filter(activated=False)
            print("Phone Numbers",phone_numbers[0])
            customer = form.save(commit=False)
            customer.primary_phone=phone_numbers[0].number
            customer.save()
            phone_numbers[0].activated=True
            phone_numbers[0].save()
            #After customer registration phone number is added as customer numbers
            CustomerNumber.objects.create(customer = customer,
            phone_number=phone_numbers[0],
            is_primary=True)
            return redirect("/")
    context = {'form':form}
    return render(request,'customer/register.html',context)

def addNumber(request,id):
    customer = Customer.objects.filter(primary_phone="01712111213")
    print(customer)
    form = BuyNumberForm()
    context = {'form':form}
    return render(request,'customer/add_number.html',context)