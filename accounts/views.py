
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.hashers import make_password

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.auth.hashers import check_password

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
            password = make_password(password)
            user_profile = UserProfile(name=name, email=email, username=username, password=password)
            user_profile.save()
            return redirect('login')
        else:
            error_message = "Passwords do not match."
            return render(request, 'accounts/signup.html', {'error_message': error_message})

    return render(request, 'accounts/signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user_profile = UserProfile.objects.get(username=username)
            if check_password(password, user_profile.password):
                # Set the session key and redirect to the user's profile page
                request.session['user_id'] = user_profile.id
                return redirect('profile')
            else:
                error_message = "Invalid password."
                return render(request, 'accounts/login.html', {'error_message': error_message})

        except UserProfile.DoesNotExist:
            error_message = "Invalid username."
            return render(request, 'accounts/login.html', {'error_message': error_message})

    return render(request, 'accounts/login.html')

@login_required
def profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user_profile = UserProfile.objects.get(pk=user_id)
    return render(request, 'accounts/profile.html', {'user_profile': user_profile})

def user_logout(request):
    auth_logout(request)
    return redirect('login')








    