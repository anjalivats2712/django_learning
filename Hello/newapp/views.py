from django.shortcuts import render,HttpResponse

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
    return render(request,'contact.htm')
    #return HttpResponse('this is contactpage')
def service(request):
    return render(request,'service.htm')
    #return HttpResponse('this is servicepage')

