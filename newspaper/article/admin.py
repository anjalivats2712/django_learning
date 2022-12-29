from django.contrib import admin
from .models import Article,Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    model=Comment

class ArticleModelAdmin(admin.ModelAdmin):
    inlines=[CommentInline]
    model=Article
    list_display=['title','body','auther']
admin.site.register(Comment)
admin.site.register(Article,ArticleModelAdmin)






