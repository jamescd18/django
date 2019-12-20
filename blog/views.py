from django.shortcuts import render
from .models import Post #in current package so '.' works

# func : HttpRequest -> HttpResponse
# Defines output for traffic to each page

def home(request):
    context = {
		'title': 'Home', # Adds custom title to browser tab label
        'posts': Post.objects.all() # Grabs list of all posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
