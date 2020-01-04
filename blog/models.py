from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# All database models for app here

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
		#if user deleted, deletes all of user's posts too
	updoots = models.SmallIntegerField(default=0)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	def upDoot(self):
		self.updoots += 1
		self.save()

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.CharField(max_length=200)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		separator = ' - '
		return post.title[:5] + separator + author.username + separator + self.content[:5]
