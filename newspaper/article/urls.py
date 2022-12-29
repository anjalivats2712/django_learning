from django.contrib import admin
from django.urls import path,include
from .views import ArticleListView,ArticleUpdateView,ArticleDeleteView,ArticleCreateView,ArticleDetailView


urlpatterns = [
    path('',ArticleListView.as_view(),name='article_home'),  
    path('<int:pk>',ArticleDetailView.as_view(),name='article_detail'),  
    path('new/',ArticleCreateView.as_view(),name='article_create'),   
    path('<int:pk>/edit/',ArticleUpdateView.as_view(),name='article_update'),   
    path('<int:pk>/delete/',ArticleDeleteView.as_view(),name='article_delete'),   
]  