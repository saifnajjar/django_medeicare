from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100, blank=True, null=True)  # Make it nullable

    def __str__(self):
        return self.username