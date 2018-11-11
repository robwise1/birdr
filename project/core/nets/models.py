from django.db import models

from stations.models import Station

class Net(models.Model):
    name = models.CharField(max_length=100)
    # location = locationfield widget or something
    notes = models.TextField()
    station = models.ForeignKey(Station, on_delete=models.CASCADE)