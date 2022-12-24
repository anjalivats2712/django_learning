from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUserModel
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUserModel
        fields=['username','email','age']
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUserModel
        fields=['username','email','age']