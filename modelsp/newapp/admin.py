from django.contrib import admin
from newapp import models
from .models import EmpInfo,AvailableJob,Project

# Register your models here.
# admin.site.register(EmpInfo)

@admin.register(EmpInfo)
class EmpInfoAdmin(admin.ModelAdmin):
    list_display=["first_name","email","working_time"]

admin.site.register(AvailableJob)
admin.site.register(Project)