from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


# Create your views here.
class SignupView(generic.CreateView):
    form_class=UserCreationForm
    template_name="signup.html"
    success_url=reverse_lazy("login")
