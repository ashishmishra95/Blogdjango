from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Created user defined form which has email field and this is inherited from UserCreationForm
class UserRegisterForm(UserCreationForm):
	# Bydefault required field for email is set to true which means is ts mandatory
	email = forms.EmailField()


	#This class will hold which model to get reflected and on what fields it would be applied so, we targeted user model with followinf fileds
	class meta:

		model = User
		fields = ['username','email','password1','password2']