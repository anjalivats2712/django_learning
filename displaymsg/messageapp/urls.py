from django.contrib import admin
from django.urls import path
from messageapp import views
from .views import Homepage

urlpatterns = [
    path('',Homepage.as_view(),name='home'),
]
