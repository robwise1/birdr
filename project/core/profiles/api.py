from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from profiles.models import User
from profiles import serializers

class UserViewSet(viewsets.ModelViewSet):
    """
    Viewset to see birds associated with a station
    """
    serializer_class = serializers.ProfileSerializer
    filter_backends = (DjangoFilterBackend, )

    def get_queryset(self):
        return User.objects.all()
