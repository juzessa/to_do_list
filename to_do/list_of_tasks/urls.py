from django.urls import path

from . import views

app_name = 'list_of_tasks'

urlpatterns = [
    path('', views.index, name='index'),
]
