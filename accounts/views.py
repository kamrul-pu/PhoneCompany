from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    context = {}
    return render(request,'accounts/home.html',context)

def userLogin(request):
    form = AuthenticationForm()
    context = {'form':form}
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect("/")
            else:
                print("User is not active")
    return render(request,'accounts/login.html',context)

@login_required
def userLogout(request):
    logout(request)
    return redirect("/")