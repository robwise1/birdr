from django.db import models
from django.contrib.auth.models import AbstractUser

from stations.models import Station

class User(AbstractUser):
    details = models.TextField(max_length=500, blank=True)
    stations = models.ManyToManyField(Station)
