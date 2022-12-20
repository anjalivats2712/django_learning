from django.contrib import admin
from django.urls import path,include
from .views import Homepage,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns = [
    path("",Homepage.as_view(),name="home"),
    path("post/<int:pk>",PostDetailView.as_view(),name="post_detail"),
    path("post/new",PostCreateView.as_view(),name="post_create"),
    path("post/update/<int:pk>",PostUpdateView.as_view(),name="post_update"),
    path("post/delete/<int:pk>",PostDeleteView.as_view(),name="post_delete"),
]