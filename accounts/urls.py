from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    

    # اضف المسارات الأخرى هنا
]