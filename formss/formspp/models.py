from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.

class UserInfo(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100,blank=True)
    phone=models.CharField(max_length=11)
    email=models.EmailField(max_length=255)

class Post(models.Model):
    title=models.CharField(max_length=100)
    auther=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    body=models.TextField()
    def __str__(self):
        return self.title[:30]
    def get_absolute_url(self):
        return reverse("blog_detail", args=[str(self.id)])
    
