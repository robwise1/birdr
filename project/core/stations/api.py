from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from stations import serializers
from stations.models import Station
from stations.services import station_service


class StationViewSet(viewsets.ModelViewSet):
    """
	Viewset to see birds associated with a station
    """
    serializer_class = serializers.StationSerializer
    filter_backends = (DjangoFilterBackend, )

    def get_queryset(self):
        return station_service.get_user_stations(self.request.user)
