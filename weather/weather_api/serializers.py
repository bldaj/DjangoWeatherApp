from rest_framework.serializers import ModelSerializer

from . import models


class WeatherSerializer(ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'
