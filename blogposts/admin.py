from django.contrib import admin

from .models import (
    BlogPost, Category, Language
)

admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(Language)
