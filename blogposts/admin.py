from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import (
    BlogPost, Category, Language
)

class BlogPostAdmin(SummernoteModelAdmin):
    summernote_fields = ['content']

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)
admin.site.register(Language)
