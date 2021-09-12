from django.contrib import admin
from django.urls import path
from notes import views
from .views import PostListView,PostDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',PostListView.as_view(),name='home'),
    path('post/<int:pk>/',PostDetailsView.as_view(),name='post_detail'),
    path('written',views.written,name='written')
]