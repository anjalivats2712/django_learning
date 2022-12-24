from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

# Create your views here.
class HomePageView(TemplateView):
    template_name='home.html'
class SignUpView(CreateView):
    form_class=CustomUserCreationForm
    template_name='signup.html'
    success_url=reverse_lazy("home")
