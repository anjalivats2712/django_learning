from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserInfo
# Create your views here.

def getInfo(request):
    if request.method=="POST":
        form=UserInfo(request.POST)
        if form.is_valid():
            return render(request,"form.html",{"form":form})
    else:
        form=UserInfo()
    return render(request,'form.html',{"form":form})

def home(request):
    return render(request,'home.html')




