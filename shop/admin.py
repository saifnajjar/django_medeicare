from django.contrib import admin
from .models import Product
from .models import Category
from .models import Comment

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
# Register your models here.
