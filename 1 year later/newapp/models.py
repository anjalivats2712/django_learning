from django.db import models

# Create your models here.

class Post(models.Model):
    name=models.CharField( max_length=50)
    content=models.TextField()
    def __str__(self):
        return self.name[:50]

class UserInfo(models.Model):
    role_in_website=[('ST','staff'),('US','user')]
    name=models.CharField(max_length=40)
    age=models.IntegerField(null=True,blank=True)
    role=models.CharField(max_length=2,choices=role_in_website)
    

