from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
# Class-Based views (CBVs)

class LoginService(View):
    def get(self, request):
        # Render the home page on GET requests
        return render(request, 'login.html', {})

    def post(self, request):
        # Handle POST requests for authentication
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In!")
            return redirect('login')  # Redirect to home page
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')  # Redirect to home page
        # redirect('home') -> looks for a named "home" in urls.py
        # Redirect to a named URL pattern
        # redirect('home')
        # # Redirect to a relative URL path
        # redirect('/some-path/')
        # # Redirect to an absolute URL
        # redirect('https://www.example.com/')
        