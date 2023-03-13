from django.shortcuts import render
from django.views.generic import ListView

from .models import (
    BlogPost
)


class BlogPostListView(ListView):
    template_name = 'blogposts/blogpost_list.html'
    model = BlogPost

