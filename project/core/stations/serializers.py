from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from stations.models import Station
from stations.services import station_service


class StationSerializer(serializers.ModelSerializer):
    details = serializers.CharField(required=False, validators=[UniqueValidator(queryset=Station.objects.all())])

    class Meta:
        model = Station
        fields = ('name', 'details')

    def create(self, validated_data):
        return station_service.create_station(self.context['request'].user, validated_data)