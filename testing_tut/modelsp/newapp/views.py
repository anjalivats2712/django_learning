from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView

# Create your views here.
# def index(request):
#     return HttpResponse('this is homepage')
class Homepage(TemplateView):
    template_name='home.htm'
class Aboutpage(TemplateView):
    template_name='about.htm'
