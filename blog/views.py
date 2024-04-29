from django.shortcuts import render
import requests
from .models import Post

from blog.models import Post


def home_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def blog_view(request):
    posts = Post.objects.filter(is_published=True)
    context = {
        'posts': posts
    }
    return render(request, 'blog.html', context=context)


def blog_single(request, pk):
    post = Post.objects.get(request=request, pk=pk)

