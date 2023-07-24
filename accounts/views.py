from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user_profile = UserProfile(name=name, email=email, username=username, password=password, confirm_password=confirm_password)
            user_profile.save()

            # يمكنك تنفيذ إجراءات إضافية هنا مثل تسجيل الدخول تلقائياً بعد التسجيل
            return redirect('login')  # تحويل المستخدم إلى صفحة تسجيل الدخول بعد التسجيل
        else:
            error_message = "كلمة المرور وتأكيد كلمة المرور غير متطابقتين."
            return render(request, 'accounts/register.html', {'error_message': error_message})

    return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # فحص بيانات تسجيل الدخول هل تتطابق مع بيانات UserProfile
        try:
            user_profile = UserProfile.objects.get(username=username, password=password)
            return redirect('departments/index')  # تحويل المستخدم إلى صفحة البداية بعد تسجيل الدخول
        except UserProfile.DoesNotExist:
            error_message = "The registration data is incorrect"
            return render(request, 'accounts/login.html', {'error_message': error_message})

    return render(request, 'accounts/login.html')




    