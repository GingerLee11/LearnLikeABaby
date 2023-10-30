from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin

from .models import (
    BlogPost, Category, Language
)

class LanguageAdmin(TranslationAdmin):
    summernote_fields = ['name']

class BlogPostAdmin(SummernoteModelAdmin, TranslationAdmin):
    summernote_fields = ['content']

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)
admin.site.register(Language, LanguageAdmin)

