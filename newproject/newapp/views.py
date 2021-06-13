from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout



# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.htm')
    #return(request,HttpResponse('this is home page'))
def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        #check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
            return redirect("/")
        else:
        # No backend authenticated the credentials
            return render(request,'login.htm')
    return render(request,'login.htm')
    #return(request,HttpResponse('this is home page'))
def logoutuser(request):
    logout(request)
    return redirect("/login")
    #return(request,HttpResponse('this is home page'))
    
