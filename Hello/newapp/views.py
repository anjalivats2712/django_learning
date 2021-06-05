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
    return HttpResponse('this is aboutpage')
def contact(request):
    return HttpResponse('this is contactpage')
def service(request):
    return HttpResponse('this is servicepage')

