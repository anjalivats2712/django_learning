from django.contrib import admin
from django.urls import path
from .views import Homepage,BlogDetailPage,BlogCreatePage,BlogUpdatePage,BlogDeletePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",Homepage.as_view(),name="home"),
    path("post/<int:pk>",BlogDetailPage.as_view(),name="blog_detail"),
    path("post/create",BlogCreatePage.as_view(),name="blog_create"),
    path("post/<int:pk>/update",BlogUpdatePage.as_view(),name="blog_update"),
    path("post/<int:pk>/delete",BlogDeletePage.as_view(),name="blog_delete"),

]
