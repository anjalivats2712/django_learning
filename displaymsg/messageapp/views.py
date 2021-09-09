from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from .models import Post

# Create your views here.
class Homepage(ListView):
    model=Post
    template_name="home.htm"
    context_object_name="all_messageapp_list"