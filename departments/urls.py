from django.urls import path
from . import views


urlpatterns = [

path('department_list/' , views.department_list , name='department_list'),
path('department/<int:department_id>/', views.department_detail, name='department_detail'),
path('all_doctors/', views.all_doctors, name='all_doctors'),
path('doctor/<int:doctor_id>/', views.doctor_detail_view, name='doctor_detail'),
path('index' , views.index , name='index'),







    




]