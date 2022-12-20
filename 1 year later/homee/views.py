from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
# def Homepage(request):
#     return HttpResponse("Homepage")
class Homepage(ListView):
    model=Post
    template_name='home.html'
    context_object_name="all_post_content"
class PostDetailView(DetailView):
    model=Post
    template_name="postdetail.html"
class PostCreateView(CreateView):
    model=Post
    template_name="postcreate.html"
    fields="__all__"
class PostUpdateView(UpdateView):
    model=Post
    template_name="postupdate.html"
    fields=['title','content']
class PostDeleteView(DeleteView):
    model=Post
    template_name="postdelete.html"
    success_url=reverse_lazy("home")
