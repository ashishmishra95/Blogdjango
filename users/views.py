from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
# Creating a register view

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			# It will save this data to databse
			form.save() 
			# If form is valid it will simply get the username record from form
			username = form.cleaned_data.get('username') 
			messages.success(request, f' Account created for { username }')
			return redirect ('blog_home')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

