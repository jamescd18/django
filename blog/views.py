from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
	ListView, DetailView, CreateView,
	UpdateView, DeleteView
)
from .models import Post #in current package so '.' works
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# func : HttpRequest -> HttpResponse
# Defines output for traffic to each page

def home(request):
    context = {
		'title': 'Home', # Adds custom title to browser tab label
        'posts': Post.objects.all() # Grabs list of all posts
    }
    return render(request, 'blog/home.html', context)

def updoot(request, **kwargs):
	pk = kwargs['pk']
	Post.objects.filter(id=pk).first().upDoot()
	origin = kwargs['origin']
	if origin == "home":
		output = redirect('/')
	elif origin == "detail":
		output = redirect('/post/'+str(pk))
	return output

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-updoots', '-date_posted'] #'-' indicates newest to oldest
	paginate_by = 5

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-updoots', '-date_posted')

class PostDetailView(DetailView):
	model = Post
	context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	context_object_name = 'post'
	fields = ['title', 'content']

	def form_valid(self, form):
		# override parent method to set author first
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	context_object_name = 'post'
	fields = ['title', 'content']

	def form_valid(self, form):
		# override parent method to set author first
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	context_object_name = 'post'
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
