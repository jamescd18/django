from django.urls import path
from . import views

# File to contain all url traffic directing for the Blog app
# Based on the django_project urls.py file starter

urlpatterns = [
    path('admin/', admin.site.urls),
]
