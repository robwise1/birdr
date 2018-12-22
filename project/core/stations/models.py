from django.db import models


from profiles.models import User

class Station(models.Model):
    """
    This represents a banding station
    """
    name = models.CharField(max_length=100, unique=True)
        # XXX Add Location Field with some widget
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='members')
    details = models.TextField(default='')

    def get_owner(self):
        return self.owner


class Net(models.Model):
    """
    Represents a physical net that belongs at a station
    """
    name = models.CharField(max_length=100)
    notes = models.TextField()
    station = models.ForeignKey(Station, on_delete=models.CASCADE)

