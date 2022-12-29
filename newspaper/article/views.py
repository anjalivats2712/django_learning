from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

# Create your views here.
class ArticleListView(ListView):
    model=Article
    template_name='articles_home.html'
    context_object_name="all_articles_list"
    login_url='login'

class ArticleDetailView(DetailView):
    model=Article
    template_name='article_detail.html'
    login_url='login'


class ArticleCreateView(LoginRequiredMixin,CreateView):
    model=Article
    fields=['title','body']
    template_name='article_create.html'
    login_url='login'

    def form_valid(self,form):
        form.instance.auther=self.request.user
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    model=Article
    fields=['title','body']
    template_name='article_edit.html'
    login_url='login'

    def dispatch(self,request,*args,**kwargs):
        obj=self.get_object
        if obj.auther != self.request.user:
            raise PermissionDenied
        else:
            return super().dispatch(request,*args,**kwargs)
  
class ArticleDeleteView(DeleteView):
    model=Article
    template_name='article_delete.html'
    success_url=reverse_lazy('home')
    login_url='login'
    
    def dispatch(self,request,*args,**kwargs):
        obj=self.get_object
        if obj.auther != self.request.user:
            raise PermissionDenied
        else:
            return super().dispatch(request,*args,**kwargs)
  
