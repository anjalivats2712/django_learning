from django.contrib import admin
from django.urls import path,include
from newapp import views

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('contact',views.ContactPageView.as_view(),name='Contact'),

]