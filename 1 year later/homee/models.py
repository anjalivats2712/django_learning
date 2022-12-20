from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=50)
    #author=models.ForeignKey("auth.user", verbose_name=_(""), on_delete=models.CASCADE)
    author=models.CharField(max_length=20)
    content=models.TextField()
    def __str__(self):
        return self.title[:50]
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
        #or use kwargs={"pk": self.pk}
    

