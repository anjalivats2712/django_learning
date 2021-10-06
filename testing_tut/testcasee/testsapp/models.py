from django.db import models


# Create your models here.

class Post(models.Model):
    text=models.TextField()

    def __str__(self):
        return self.text[:50]
class Info(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=255)
    phone=models.CharField(max_length=11)
    
    def __str__(self):
        return self.name[:50]


