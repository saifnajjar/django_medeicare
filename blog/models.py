from django.db import models

# اضف الاختيارات للتصنيفات
CATEGORY_CHOICES = [
    ('Economy', 'Economy'),
    ('Sport', 'Sport'),
    ('Technology', 'Technology'),
    ('Travel', 'Travel'),
    ('Lifestyle', 'Lifestyle'),
]

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"        





       
