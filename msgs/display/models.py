from django.db import models
from django.db.models.fields import TextField
from django.db import models

# Create your models here.
class Msgs(models.Model):
    email=models.CharField(max_length=122,default="",editable=False)
    text=models.TextField()
    
    def __str__(self):
        return self.text[:20]
    


