from django.contrib import admin
from .models import UserInfo

# Register your models here.
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display=["first_name","phone","email"]
    list_filter=["first_name","email"]
    search_fields=["first_name","last_name","email"]
