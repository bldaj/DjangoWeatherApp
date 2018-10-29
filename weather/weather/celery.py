import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')


app = Celery('weather')
app.autodiscover_tasks()

app.config_from_object('django.conf:settings')

app.conf.beat_schedule = {
    'abc': {
        'task': 'weather_app.tasks.test',
        'schedule': 5,
        'args': ()
    },
    'populate_db': {
        'task': 'weather_app.tasks.populate_db',
        'schedule': 20,
        'args': ()
    }
}
