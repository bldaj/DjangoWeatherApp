from datetime import datetime

import requests
from celery import shared_task

from weather_api import models


@shared_task
def test():
    print('TEST')


@shared_task
def populate_db():
    url = 'http://api.openweathermap.org/data/2.5/forecast?q={0}&units=metric&appid=f3e26c0ee52a2763f0a05af1a1446a0d'

    with open('weather_app/cities.txt') as cities_file:
        for city in cities_file:

            city = city.replace('\n', '')

            city_weather_for_3_hours = requests.get(url.format(city)).json()

            if city_weather_for_3_hours['cod'] != '404' and city_weather_for_3_hours['cod'] != 401:
                for weather_for_3_hour in city_weather_for_3_hours['list']:
                    dt = datetime.strptime(weather_for_3_hour['dt_txt'], '%Y-%m-%d %H:%M:%S')
                    temp = weather_for_3_hour['main']['temp']
                    temp_min = weather_for_3_hour['main']['temp_min']
                    temp_max = weather_for_3_hour['main']['temp_max']

                    models.City(name=city, date=dt, temp=temp, temp_min=temp_min, temp_max=temp_max).save()
