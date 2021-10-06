from django.db import models

# Create your models here.

class UserInfo(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100,blank=True)
    phone=models.CharField(max_length=11)
    email=models.EmailField(max_length=255)
    
