from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
	ListView, DetailView, CreateView,
	UpdateView, DeleteView
)
from .models import Post, Comment #in current package so '.' works
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CommentPostForm
from django.contrib import messages

# func : HttpRequest -> HttpResponse
# Defines output for traffic to each page

def home(request):
    context = {
		'title': 'Home', # Adds custom title to browser tab label
        'posts': Post.objects.all() # Grabs list of all posts
    }
    return render(request, 'blog/home.html', context)

@login_required
def updoot(request, **kwargs):
	pk = kwargs['pk']
	Post.objects.get(id=pk).upDoot()
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

def postDetail(request, **kwargs):
	post = get_object_or_404(Post, id=kwargs.get('pk'))
	if request.method == 'POST':
		c_form = CommentPostForm(request.POST, instance=request.user)
		if c_form.is_valid(request, post):
			com = Comment(post=post, author=request.user,
						  content=c_form.cleaned_data.get('content'))
			com.save()
			messages.success(request, f'Comment posted!')
			return redirect('post-detail', kwargs.get('pk')) # So won't re-run post request if page reloaded
	else:
		c_form = CommentPostForm(instance=request.user)
	context = {
		'title': post.title,
		'post': post,
		'comments': Comment.objects.filter(post=post),
		'c_form': c_form
	}
	return render(request, 'blog/post_detail.html', context)

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
