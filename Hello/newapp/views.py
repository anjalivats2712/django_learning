from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('this is homepage')
def about(request):
    return HttpResponse('this is aboutpage')
def contact(request):
    return HttpResponse('this is contactpage')
def service(request):
    return HttpResponse('this is servicepage')

