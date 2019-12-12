from django.shortcuts import render

posts = [
    {
        'author': 'James CD',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 11, 2019'
    },
    {
        'author': 'Pepper B.',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'December 7, 2019'
    }
]

# func : HttpRequest -> HttpResponse
# Defines output for traffic to each page

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
