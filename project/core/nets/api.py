from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from nets.models import Net
from nets import serializers

class NetViewSet(viewsets.ModelViewSet):
    """
    Viewset to see birds associated with a station
    """
    serializer_class = serializers.NetSerializer
    filter_backends = (DjangoFilterBackend, )

    def get_queryset(self):
        return Net.objects.all()
