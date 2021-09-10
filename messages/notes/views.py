from notes.models import Msgs
from django.db.models.base import Model
from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,TemplateView
from django.contrib import messages

# Create your views here.
class Index(ListView):
    model=Msgs
    template_name='index.htm'
    context_object_name='all_msgs_list'
def written(request):
    if request.method=="POST":
        email=request.POST.get('email')
        text=request.POST.get('text')
        anjali=Msgs(email=email,text=text)
        anjali.save()
        messages.success(request,"your message has been sent.Please refresh the page to see yours.")

    return render(request,"written.htm")

