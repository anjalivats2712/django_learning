from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User, UserManager
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout



# Create your views here.

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        print('the user is anonymous')
        return redirect("/login")
    return render(request,'login.htm')
    #return(request,HttpResponse('this is home page'))
def loginuser(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username,password)

        #check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
            login(request, user)
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
    
