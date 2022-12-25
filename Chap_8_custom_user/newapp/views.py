from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.core.mail import send_mail,EmailMessage

# Create your views here.
class HomePageView(TemplateView):
    template_name='home.html'
class SignUpView(CreateView):
    form_class=CustomUserCreationForm
    template_name='signup.html'
    success_url=reverse_lazy("home")
def sendAnEmail(request):
    send_mail('hello','hello everyone','anjalivats1227@gmail.com',['20bec017@nith.ac.in'],fail_silently=False)

    return HttpResponse("your mail has been sent")
