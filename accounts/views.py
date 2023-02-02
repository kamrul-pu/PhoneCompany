from django.shortcuts import render

# Create your views here.

def userLogin(request):
    return render(request,'accounts/login.html')