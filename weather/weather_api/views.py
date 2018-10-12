from rest_framework import viewsets

from . import serializers
from .models import City


class WeatherViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WeatherSerializer

    def get_queryset(self):
        queryset = City.objects.all()

        city_name = self.request.query_params.get('name', None)

        if city_name is not None:
            queryset = queryset.filter(name__contains=city_name)

        return queryset
