from django.contrib import admin
from django.urls import path
from newapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("forms",views.getInfo,name="form")
]