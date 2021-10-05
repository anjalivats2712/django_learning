from django.db import models

# Create your models here.

class EmpInfo(models.Model):
    GEN_CHOICE=[('M',"Morning"),('A',"Afternoon"),('E',"Evening")]
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100,blank=True)
    email=models.EmailField(max_length=255)
    gender=models.CharField(max_length=6,blank=True)
    working_time=models.CharField(choices=GEN_CHOICE,default="M",max_length=1)
    emp_job=models.ManyToManyField('AvailableJob',blank=True)

    def __str__(self):
        return self.first_name[:50]

class AvailableJob(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name[:50]

class Project(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/")
    description=models.TextField()
    # def __str__(self):
    #     return self.title[:50]
    