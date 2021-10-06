from django.contrib import admin
from .models import Info, Post
# Register your models here.
admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display=['name','phone','email']
    search_fields=['name','email']
    list_filter=["name","email"]