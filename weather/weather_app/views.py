from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponse

from weather.celery import populate_db, test_task


def index(request, **context):
    return render(request, 'weather_app/index.html')


def run_script(request):
    populate_db.delay()
    return redirect(reverse('weather:index'), permanent=True)
    # return HttpResponse('Task has begun')
