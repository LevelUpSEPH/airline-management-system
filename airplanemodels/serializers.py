from rest_framework import serializers
from .models import AirplaneModel

class AirplaneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneModel
        fields = ['id', 'name']