from django.shortcuts import render
from django.views.generic import ListView, DetailView

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


class BlogPostDetailView(DetailView):
    """
    Shows the details of the Blog post
    """
    template_name = 'blogposts/blogpost_detail.html'
    model = BlogPost
    context_object_name = 'blogpost'

