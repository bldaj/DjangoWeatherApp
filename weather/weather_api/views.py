from rest_framework import viewsets

from . import serializers
from .models import City


class WeatherViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WeatherSerializer

    def get_queryset(self):
        queryset = City.objects.all()

        city_name = self.request.query_params.get('name', None)
        day = self.request.query_params.get('day', None)

        if city_name is not None:
            queryset = queryset.filter(name__iexact=city_name)

        if day is not None:
            queryset = queryset.filter(date__day=day)

        return queryset
