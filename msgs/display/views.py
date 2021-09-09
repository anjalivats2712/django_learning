from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,TemplateView
from .models import Msgs

# Create your views here.
def index(request):
    return HttpResponse('this is home page')
class Homepage(ListView):
    model=Msgs
    template_name='index.htm'
    context_object_name='all_msgs_list'
def written(request):
    if request=='POST':
        email=request.get.POST("email")
        text=request.get.POST("text")
        written=Msgs(email=email,text=text)
        written.save()
    return render(request,'written.htm')
