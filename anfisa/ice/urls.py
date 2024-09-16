from django.urls import path

from . import views

app_name = 'ice'

urlpatterns = [
    path('', views.index, name='index'),
]
