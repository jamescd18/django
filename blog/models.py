from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# All database models for app here

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
		#if user deleted, deletes all of user's posts too

	def __str__(self):
		return self.title
