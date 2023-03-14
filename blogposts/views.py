from django.shortcuts import render
from django.views.generic import ListView

from .models import (
    BlogPost
)


class BlogPostListView(ListView):
    """
    Shows a list of all the blogposts 
    ordered by date published and author.
    """
    template_name = 'blogposts/blogpost_list.html'
    model = BlogPost

