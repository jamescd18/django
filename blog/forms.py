from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment

class CommentPostForm(forms.ModelForm):
	content = forms.CharField(max_length=200)

	def is_valid(self, request, post):
		# override parent method to set author first
		self.instance.author = request.user
		self.instance.post = post
		return super().is_valid()

	class Meta:
		model = Comment
		fields = ['content']
