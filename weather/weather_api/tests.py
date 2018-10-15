from datetime import datetime

from rest_framework.test import APITestCase

from .models import City


def create_city(name, date):
    return City.objects.create(name=name, date=date)


def convert_datetime_to_str(date: datetime):
    return date.strftime('%Y-%m-%dT%H:%M:%S.%f')


def convert_ordered_dict_to_list_of_dicts(ordered_dict_list: list):
    dicts_list = []

    for ordered_dict in ordered_dict_list:
        dicts_list.append(dict(ordered_dict))

    return dicts_list


class TestWeatherApi(APITestCase):

    def test_get_all_weather_data_for_all_cities(self):
        cities = [
            {
                'name': 'andorra',
                'date': datetime.now(),
                'temp': -278.0,
                'temp_min': -278.0,
                'temp_max': -278.0
            },
            {
                'name': 'aixirivall',
                'date': datetime.now(),
                'temp': -278.0,
                'temp_min': -278.0,
                'temp_max': -278.0
            }
        ]

        for city in cities:
            create_city(name=city['name'], date=city['date'])

        for city in cities:
            city['date'] = convert_datetime_to_str(city['date'])

        response = self.client.get('/weather/')

        self.assertEqual(
            cities,
            convert_ordered_dict_to_list_of_dicts(list(response.data['results']))
        )

    def test_get_all_weather_for_one_city(self):
        cities = [
            {
                'name': 'andorra',
                'date': datetime.now(),
                'temp': -278.0,
                'temp_min': -278.0,
                'temp_max': -278.0
            },
            {
                'name': 'aixirivall',
                'date': datetime.now(),
                'temp': -278.0,
                'temp_min': -278.0,
                'temp_max': -278.0
            }
        ]

        for city in cities:
            create_city(name=city['name'], date=city['date'])

        cities[0]['date'] = convert_datetime_to_str(cities[0]['date'])

        response = self.client.get('/weather/?name={0}'.format(cities[0]['name']))

        dicts_list = convert_ordered_dict_to_list_of_dicts(list(response.data['results']))

        if len(dicts_list) == 1:
            self.assertEqual(
                cities[0],
                dicts_list[0]
            )

    def test_get_all_weather_for_one_city_and_one_day(self):
        cities = [
            {
                'name': 'andorra',
                'date': datetime.now(),
                'temp': -278.0,
                'temp_min': -278.0,
                'temp_max': -278.0
            },
            {
                'name': 'andorra',
                'date': datetime.now(),
                'temp': -278.0,
                'temp_min': -278.0,
                'temp_max': -278.0
            },
            {
                'name': 'aixirivall',
                'date': datetime.now(),
                'temp': -278.0,
                'temp_min': -278.0,
                'temp_max': -278.0
            }
        ]

        for city in cities:
            create_city(name=city['name'], date=city['date'])

        for city in cities:
            city['date'] = convert_datetime_to_str(city['date'])

        response = self.client.get('/weather/?name={0}&day={1}'.format(cities[0]['name'], datetime.now().day))

        dicts_list = convert_ordered_dict_to_list_of_dicts(list(response.data['results']))

        if len(dicts_list) == 2:
            self.assertEqual(
                cities[0:2],
                dicts_list
            )
