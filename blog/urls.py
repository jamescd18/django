from django.urls import path
from .views import PostListView, PostDetailView
from . import views

# File to contain all url traffic directing for the Blog app
# Based on the django_project urls.py file starter

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
				# pk is primary key, specified to be an integer
    path('about/', views.about, name='blog-about'),
]
