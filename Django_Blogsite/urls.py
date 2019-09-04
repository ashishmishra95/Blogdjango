"""Django_Blogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# To tell our application which path to route we have to use (include) function and add the specific paths to it
from django.urls import path,include
# We are importing our register view page
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register, name = 'register'),
    path('', include('blog.urls')), #It will be always a string
    #To make our user redirected to home page without doing any routing (i.e by just visiting site)we can do thi like:
    #path('', include('blod.urls')) 

]
 