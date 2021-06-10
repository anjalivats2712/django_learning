from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.htm')
    #return(request,HttpResponse('this is home page'))
def login(request):
    return render(request,'login.htm')
    #return(request,HttpResponse('this is home page'))
def logout(request):
    return render(request,'logout.htm')
    #return(request,HttpResponse('this is home page'))
    
