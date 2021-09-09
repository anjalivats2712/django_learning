from django.contrib import admin
from django.urls import path
from notes import views
from .views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index.as_view(),name='index'),
    path('written',views.written,name='written')
]
