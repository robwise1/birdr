from rest_framework import serializers

from birds.models import Bird


class BirdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bird
        fields = '__all__'