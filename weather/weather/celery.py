import os
from datetime import datetime

import requests
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')


app = Celery('weather')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, populate_db.s(), name='Populate every 30 minutes')


@app.task
def test_task(txt):
    print(txt)


@app.task
def populate_db():
    from weather_api import models

    url = 'http://api.openweathermap.org/data/2.5/forecast?q={0}&appid=d0068bdfb3a12607733e3b32622f9ac2'

    with open('weather/cities.txt') as cities_file:
        for city in cities_file:
            city_weather_for_3_hours = requests.get(url.format(city)).json()

            if city_weather_for_3_hours['cod'] != '404':
                for weather_for_3_hour in city_weather_for_3_hours['list']:
                    dt = datetime.strptime(weather_for_3_hour['dt_txt'], '%Y-%m-%d %H:%M:%S')
                    models.City(name=city, date=dt).save()
                break
