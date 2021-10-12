from django import forms
# from django.contrib.auth.forms import UserCreationForm,UserChangeForm


# from .models import CustomUserModel

# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model=CustomUserModel
#         fields=UserCreationForm.Meta.fields + 'age'
# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model=CustomUserModel
#         fields=UserChangeForm.Meta.fields + 'age'

class UserInfo(forms.Form):
    name=forms.CharField(max_length=100,label="name")
    year=forms.IntegerField(max_value=4,label="year")
    branch=forms.CharField(max_length=3,label="branch")

    def __str__(self):
        return self.name