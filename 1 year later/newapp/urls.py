from django.contrib import admin
from django.urls import path,include
from newapp import views
from .views import HomePageView, ContactPageView,QueryPageView,ListPageView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('contact',ContactPageView.as_view(),name='Contact'),
    path('query',QueryPageView.as_view(),name='Query'),
    path('list',ListPageView.as_view(),name='list'),

]