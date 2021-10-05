from django.contrib import admin
from newapp import models
from .models import EmpInfo,AvailableJob,Project

# Register your models here.
# admin.site.register(EmpInfo)

@admin.register(EmpInfo)
class EmpInfoAdmin(admin.ModelAdmin):
    list_display=["first_name","email","working_time"]

admin.site.register(AvailableJob)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['title']
    search_fields=['title','description']
    list_filter=['title']
