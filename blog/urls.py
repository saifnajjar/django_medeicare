from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),
    
    # ... يمكنك إضافة المزيد من أوامر الـ URL هنا ...
]





