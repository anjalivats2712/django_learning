from django.contrib import admin
from django.urls import path
from .views import Homepage,Aboutpage,BlogDetailPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",Homepage.as_view(),name="home"),
    path("about",Aboutpage.as_view(),name="about"),
    path("post/<int:pk>",BlogDetailPage.as_view(),name="blog_detail")
]
