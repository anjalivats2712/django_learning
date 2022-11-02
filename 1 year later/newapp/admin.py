from django.contrib import admin
from .models import Post,UserInfo

# Register your models here.
admin.site.register(Post)

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display= ['name','age','role']
    list_filter= ['age','role']
    search_fields=['name']


