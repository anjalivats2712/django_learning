from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request,'index.htm')
    #return(request,HttpResponse('this is home page'))
def login(request):
    # if request.method=="POST":
    #     username=request.POST.get("username")
    #     password=request.POST.get("password")

    #     #check if user has entered correct credentials
    #     user = authenticate(username=username, password=password)
    return render(request,'login.htm')
    #return(request,HttpResponse('this is home page'))
def logout(request):
    return render(request,'logout.htm')
    #return(request,HttpResponse('this is home page'))
    
