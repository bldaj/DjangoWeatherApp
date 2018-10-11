from rest_framework.serializers import ModelSerializer

from .models import City


class WeatherSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ('name', 'date')
