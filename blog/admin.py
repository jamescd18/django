from django.contrib import admin
from .models import Post, Comment

# Control things that are visible in the admin dashboard
# Groups for permissioning & user included by default

admin.site.register(Post)
admin.site.register(Comment)
