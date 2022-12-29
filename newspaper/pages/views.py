from django.shortcuts import render,HttpResponse

# Create your views here.
def homePage(request):
    return render(request,'home.html')