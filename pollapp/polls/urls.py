from django.urls import path

from . import views

app_name = 'polls'
urlpattern = [
    path('', views.index, name='index')
]
