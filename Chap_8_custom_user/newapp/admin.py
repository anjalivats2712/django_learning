from django.contrib import admin
from .models import CustomUserModel
from .forms import CustomUserChangeForm,CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUserModel
    list_display=['username','email','age']




admin.site.register(CustomUserModel,)
