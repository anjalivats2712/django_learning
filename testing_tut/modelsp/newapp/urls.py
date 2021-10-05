from django.contrib import admin
from django.urls import path
from newapp import views
from .views import Homepage,Aboutpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",Homepage.as_view(),name='home'),
    path("about",Aboutpage.as_view(),name='about'),
    
]
