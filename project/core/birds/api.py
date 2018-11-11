from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from birds.models import Bird
from birds import serializers

class BirdViewSet(viewsets.ModelViewSet):
    """
    Viewset to see birds associated with a station
    """
    serializer_class = serializers.BirdSerializer
    filter_backends = (DjangoFilterBackend, )

    def get_queryset(self):
        return Bird.objects.all()
