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
def written(request):
    if request.method=="POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        body=request.POST.get('body')
        anjali=Post(title=title,author=author,body=body)
        anjali.save()
    return render(request,"written.html")
