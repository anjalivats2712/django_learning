from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic.detail import DetailView

from formspp.models import Post

# Create your views here.
class Homepage(ListView):
    template_name="home.html"
    model=Post
    context_object_name="all_post_list"

class Aboutpage(TemplateView):
    template_name="about.htm"

class BlogDetailPage(DetailView):
    model=Post
    template_name="detail.html"
