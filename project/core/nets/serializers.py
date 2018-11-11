from rest_framework import serializers

from nets.models import Net

class NetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Net
		fields = '__all__'