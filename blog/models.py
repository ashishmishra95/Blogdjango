# imported post model
from django.db import models 
from django.utils import timezone # for current dates on each post
#imported user model
from django.contrib.auth.models import User


# Create your models here.
# We are creating models for post which contains title,content,descripion etc 
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete= models.CASCADE) # on deletinf post will this be deleting user too


# To make our post details descriptive for shell we can use
	def __str__(self):
		return self.title