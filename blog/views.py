from django.shortcuts import render

from .models import *

# Create your views here.

def frontpage(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'frontpage.html', context)


def detail(request, slug):
    post = Post.objects.get(slug=slug)

    context = {
        'post': post
    }

    return render(request, 'detail.html', context)


def category(request, slug):
    category = Category.objects.get(slug=slug)

    context = {
        'category': category
    }

    return render(request, 'category.html', context)