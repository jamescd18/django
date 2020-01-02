from django.urls import path
from .views import (
	PostListView, PostDetailView, PostCreateView,
	PostUpdateView, PostDeleteView
)
from . import views

# File to contain all url traffic directing for the Blog app
# Based on the django_project urls.py file starter

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
				# pk is primary key, specified to be an integer
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('post/<int:pk>/<str:origin>/updoot/', views.updoot, name='post-updoot'),
    path('about/', views.about, name='blog-about'),
]
