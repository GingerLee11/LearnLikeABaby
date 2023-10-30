from modeltranslation.translator import register, TranslationOptions
from .models import BlogPost, Language


@register(BlogPost)
class BlogPostTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'content',)


@register(Language)
class LanguageTranslationOptions(TranslationOptions):
    fields = ('name',)
