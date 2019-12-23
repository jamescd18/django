from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	#fname = forms.Text()
	#lname = forms.Text()
	#age = forms.DatePicker()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']#'fname', 'lname', 'age', 
