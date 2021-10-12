from django import forms
from django.shortcuts import render,HttpResponse
from .forms import UserInfo

# Create your views here.
def getInfo(request):
    if request.method=="POST":
        form=UserInfo(request.POST)
        if form.is_valid():
            # return render(request,"form.html",{"form":form})
            name=form.cleaned_data['name']
            year=form.cleaned_data['year']
            branch=form.cleaned_data['branch']
            return render(request,'info.html',{"name":name,"year":year,"branch":branch})
    else:
        form=UserInfo()
    return render(request,"forms.html",{"form":form})
    
def home(request):
    return render(request,"home.html")