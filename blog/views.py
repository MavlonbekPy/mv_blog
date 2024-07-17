from django.shortcuts import render
from .models import Post


def home_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def blog_view(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'blog.html', context=context)


def blog_single(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog-single.html', context={'post': post})
