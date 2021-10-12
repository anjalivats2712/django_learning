from django.contrib import admin
from django.urls import path

from viki import views

urlpatterns = [
  path("",views.home,name="home"),
  path("form",views.getInfo,name="form")
]
