from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

#We are creating dummy data that can be accessed through our template which we have rendered

# posts = [
# 	{
# 			'author': 'Ashish Mishra',
# 			'date_posted':'16-08-2019',
# 			'title':'Blog post 1',
# 			'content':'This is gonna be viral soon!',

# 	},
# 	{	
# 			'author':'Ghanshyam Gupta',
# 			'date_posted':'16-08-2019',
# 			'title':'Blog post 2',
# 			'content':'Yeah actually',

# 	}

# ]

# abouts = [

# 		{
# 			'author':'Ashish',
# 			'designation':'CEO',
# 			'company':'The Startup',
# 			'spouse':'Varsha',
# 		},






# ]

# Whenever users lands on Home HttpResponse should handles it 
def home(request):
	# Whatever we have defined we are accessing from here
	context = {
	'posts':  Post.objects.all(),#posts, # key (posts)
	}
	# Loading of template in another way using render function which take 2 arguments i.e request and template which we want to fetch
	return render(request, 'blog/home.html',context) # we used sub folder name which we have created under templated folder i.e blog
	#return HttpResponse('<h1>Blog Home</h1>')

# Adding About page 


def about(request):
	#return HttpResponse('<h1>Blog About</h1>')
	# context2 = {
	# 	'abouts': abouts,
	# }
	return render(request, 'blog/about.html',{'title':'About Us'})
	# return render (request, 'blog/about.html',context2)



