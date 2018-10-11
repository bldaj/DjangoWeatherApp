from rest_framework import viewsets
from django.shortcuts import render

from . import serializers
from .models import City


class WeatherViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = serializers.WeatherSerializer
