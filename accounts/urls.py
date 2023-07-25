from django.urls import path
from . import views

urlpatterns = [
    # توجيه URL لصفحة التسجيل
    path('register/', views.register, name='register'),

    # توجيه URL لصفحة تسجيل الدخول
    path('', views.user_login, name='login'),

    # توجيه URL لصفحة البروفايل بعد تسجيل الدخول بنجاح
    path('profile/', views.profile, name='profile'),

    # توجيه URL لصفحة تسجيل الخروج
    path('logout/', views.user_logout, name='logout'),
]