from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from formspp.models import Post

# Create your views here.
class Homepage(ListView):
    template_name="home.html"
    model=Post
    context_object_name="all_post_list"

class BlogDetailPage(DetailView):
    model=Post
    template_name="detail.html"

class BlogCreatePage(CreateView):
    model=Post
    template_name="write.html"
    fields="__all__"#we use this when we include {{form.as_p}} in html templates, all means we are including all fields in p
class BlogUpdatePage(UpdateView):
    model=Post
    template_name="update.html"
    fields=["title",'body']#this means we are adding only selected fields in p
class BlogDeletePage(DeleteView):
    model=Post
    template_name="delete.html"
    success_url=reverse_lazy("home")#we want to give enough time to server before it deletes the post and takes us to the homepage
