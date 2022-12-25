from django.contrib import admin
from django.urls import path,include
from .views import HomePageView,SignUpView,sendAnEmail

urlpatterns = [
    path('signup',SignUpView.as_view(),name="signup"),
    path('email',sendAnEmail,name="semail"),
    
]