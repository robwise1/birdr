from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    details = models.TextField(max_length=500, blank=True)
