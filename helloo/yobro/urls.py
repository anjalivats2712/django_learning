from django.contrib import admin
from django.urls import path
from yobro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("aboutf/",views.about,name="about")
]