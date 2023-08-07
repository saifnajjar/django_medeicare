
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from .decorators import login_required

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            # Create a new user profile and save it to the database
            user = User.objects.create_user(username=username, email=email, password=password, first_name=name)
            return redirect('login')
        else:
            error_message = "Passwords do not match."
            return render(request, 'accounts/signup.html', {'error_message': error_message})

    return render(request, 'accounts/signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('profile')
        else:
            error_message = "Invalid username or password."
            return render(request, 'accounts/login.html', {'error_message': error_message})

    return render(request, 'accounts/login.html')

@login_required
def profile(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user': user})

def user_logout(request):
    auth_logout(request)
    return redirect('login')







    