from django.shortcuts import render

from .models import *

# Create your views here.

def frontpage(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'frontpage.html', context)