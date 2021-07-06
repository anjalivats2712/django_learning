from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
class homepage(ListView):
    template_name="home.htm"