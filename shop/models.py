from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/', null=True, blank=True)  # اسم مجلد الصور هو 'products/'
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)  # حقل الكمية
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default='This is a default description.')  # Add the default value here

    def __str__(self):
        return self.name



from django.db import models

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)

    title = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.title        
