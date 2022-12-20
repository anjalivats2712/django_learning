from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView,ListView
from .models import UserInfo

# Create your views here.
# def Homepage(request):
#     return HttpResponse("hello user")
# def Contactpage(request):
#     return HttpResponse("u can contact us through our mail")
class HomePageView(TemplateView):
    template_name= 'Homepage.html'
class ContactPageView(TemplateView):
    template_name='contactpage.html'

class QueryPageView(TemplateView):
    template_name='querypage.html'
class ListPageView(ListView):
    model=UserInfo
    template_name='list_of_workers.html'
    context_object_name="all_workers_name"



