from django.contrib import admin
from django.urls import path
from newapp import views
from .views import New

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('service',views.service,name="service"),
    path("new",New.as_view(),name="new"),


]