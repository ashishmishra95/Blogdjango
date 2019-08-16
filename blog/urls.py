from django.urls import path
 # We will import our Home views from views.py (.) is to represent current directory
from . import views
# We have added home function defined in views.py into our path have simply called it using views.home and have also assigned a named to it
urlpatterns = [
    path('', views.home, name = 'blog_home'),
    path('about/', views.about, name = 'blog_about'),

]