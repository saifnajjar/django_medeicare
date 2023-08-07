from django.urls import path
from . import views




from django.urls import path
from . import views

urlpatterns = [
    path('', views.pharmacy, name='pharmacy'),

     path('product/<int:product_id>/', views.product_detail, name='product_detail'),
     path('product/<int:product_id>/add_review/', views.add_review, name='add_review'),
     


]



