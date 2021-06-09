from django.shortcuts import render,HttpResponse
from datetime import datetime
from newapp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'variable' :'this is sent',
        'variable2':'this is not done',
    }
    return render(request,'index.htm',context)
    #return HttpResponse('this is homepage')
def about(request):
    return render(request,'about.htm')
    #return HttpResponse('this is aboutpage')
def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        query=request.POST.get('query')
        contact=Contact(name=name,email=email,query=query,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!Thanku for contacting us.')

        
    return render(request,'contact.htm')
    #return HttpResponse('this is contactpage')
def service(request):
    return render(request,'service.htm')
    #return HttpResponse('this is servicepage')

