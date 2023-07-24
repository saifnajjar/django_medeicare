from django.urls import path
from . import views


urlpatterns = [

path('BLOG_GRID/' , views.BLOG_GRID , name='BLOG_GRID'),
path('BLOG_LIST/' ,views.BLOG_LIST , name='BLOG_LIST'),
path('SINGLE_POST/' ,views.SINGLE_POST , name='SINGLE_POST'),

]