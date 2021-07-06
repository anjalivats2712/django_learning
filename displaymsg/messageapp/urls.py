from django.contrib import admin
from django.urls import path
from messageapp import views
from .views import homepage

urlpatterns = [
    path('',homepage.as_view(),name='home'),
]
