from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post #in current package so '.' works

# func : HttpRequest -> HttpResponse
# Defines output for traffic to each page

def home(request):
    context = {
		'title': 'Home', # Adds custom title to browser tab label
        'posts': Post.objects.all() # Grabs list of all posts
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted'] #'-' indicates newest to oldest

class PostDetailView(DetailView):
	model = Post
	context_object_name = 'post'

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
