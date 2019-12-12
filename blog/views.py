from django.shortcuts import render
from .models import Post #in current package so '.' works

# func : HttpRequest -> HttpResponse
# Defines output for traffic to each page

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
