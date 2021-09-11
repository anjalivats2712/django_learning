from django.shortcuts import render
from django.views.generic import ListView,DetailView
from notes.models import Post

# Create your views here.
class PostListView(ListView):
    model=Post
    template_name='index.html'
    context_object_name='all_posts_list'

class PostDetailsView(DetailView):
    model=Post
    template_name='detailview.html'
