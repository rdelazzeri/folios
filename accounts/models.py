# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    slug = models.SlugField(max_length=60)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username