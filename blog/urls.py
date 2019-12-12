from django.urls import path
from . import views

# File to contain all url traffic directing for the Blog app
# Based on the django_project urls.py file starter

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
