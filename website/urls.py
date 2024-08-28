from django.urls import path
from . views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', LoginService.as_view(), name = 'login'),

    path('logout/', LogoutView.as_view(next_page='/'), name='logout'), # Logs out the current user by calling Django's logout() function.
    # Root URL (/): The root URL '/' is the top-level URL of a web application. 
    # It is the first URL that is loaded when you visit a domain without specifying any additional path. 
    # For example, if your domain is example.com, navigating to example.com/ will take you to the homepage.
]
