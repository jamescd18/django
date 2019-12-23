from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

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
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Profile successfully updated!')
			return redirect('profile') # So won't re-run post request if page reloaded
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/profile.html', context)
