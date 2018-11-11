from rest_framework import serializers

from profiles.models import User


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'