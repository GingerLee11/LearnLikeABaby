from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=200)

    def __str__(self):
        return f"{self.name}"


class Language(models.Model):
    name = models.CharField(_("Language Name"), max_length=150)

    def __str__(self):
        return f"{self.name}"


class BlogPost(models.Model):
    """
    Model for creating blog posts
    """
    title = models.CharField(_("Title"), max_length=150)
    sub_title = models.CharField(_("Sub-title"), max_length=300, blank=True, null=True)
    category = models.ManyToManyField("Category", blank=True)
    language = models.ManyToManyField("Language", help_text="What languages is this blogpost available in?")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_published = models.DateTimeField(_("Published"), auto_now_add=True)
    date_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
    content = models.TextField(_("Content"))

    def __str__(self):
        return f"Title: {self.title}, Sub-title: {self.sub_title}"
    
    class Meta:
        ordering = ['-date_published', 'author']


