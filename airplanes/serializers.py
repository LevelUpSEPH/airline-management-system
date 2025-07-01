from rest_framework import serializers
from .models import Airplane
from airplanemodels.models import AirplaneModel
from airplanemodels.serializers import AirplaneModelSerializer

class AirplaneSerializer(serializers.ModelSerializer):
    model = AirplaneModelSerializer(read_only=True)

    model_id = serializers.PrimaryKeyRelatedField(
        source='model',
        queryset=AirplaneModel.objects.all(),
        write_only=True
    )

    class Meta:
        model = Airplane
        fields = ['id', 'tail_number', 'model', 'model_id', 'capacity', 'production_year', 'status']
        read_only = ['id']