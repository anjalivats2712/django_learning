from django.contrib import admin
from .models import Post, UserInfo

# Register your models here.
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display=["first_name","phone","email"]
    list_filter=["first_name","email"]
    search_fields=["first_name","last_name","email"]
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title',"auther"]
    list_filter=['title',"auther"]
    search_fields=['title',"auther"]