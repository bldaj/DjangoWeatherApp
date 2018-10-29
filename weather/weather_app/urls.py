from django.urls import path

from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.index, name='index'),
    path('run/', views.run_script, name='run_script')
]
