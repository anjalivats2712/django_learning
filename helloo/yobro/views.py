from django.shortcuts import render,HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("Hello, world. f4d22497 is the polls index.")

def home(request):
    # return render(request,HttpResponse("hello world"))
    return render(request,"home.html")

def about(request):

    return render(request,"about.html",{"ab":"/about"})

