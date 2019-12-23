from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save() # Saves the user
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! Login below.')
				# Outputs success message
			return redirect('login')
	else:
		form = UserRegisterForm()
	context = {
		'form': form
	}
	return render(request, 'users/register.html', context)


@login_required # Decuractor added functionality to this method
def profile(request):
	return render(request, 'users/profile.html')
