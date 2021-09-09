from typing import Text
from django.db import models

# Create your models here.
class Msgs(models.Model):
    email=models.CharField(max_length=122)
    text=models.TextField()
