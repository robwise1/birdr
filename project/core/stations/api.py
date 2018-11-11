from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from stations.models import Station
from stations import serializers

class StationViewSet(viewsets.ModelViewSet):
    """
	Viewset to see birds associated with a station
    """
    serializer_class = serializers.StationSerializer
    filter_backends = (DjangoFilterBackend, )

    def get_queryset(self):
        return Station.objects.all()
