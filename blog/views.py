from django.shortcuts import render
from django.http import HttpResponse

# home : HttpRequest -> HttpResponse
# Defines output for traffic to the Blog home page
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')
