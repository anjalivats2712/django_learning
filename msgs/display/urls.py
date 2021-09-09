from django.contrib import admin
from django.urls import path
from display import views
from .views import Homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Homepage.as_view(),name='index'),
    path('written',views.written,name='msg')
]
