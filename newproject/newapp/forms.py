from django import forms 

class UserInfo(forms.Form):
    name=forms.CharField(label="name",max_length=100)
    year=forms.IntegerField(label="year",max_value=4)
    branch=forms.CharField(label="branch",max_length=4)