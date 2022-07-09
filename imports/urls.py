from django.urls import path

from . import views

app_name = 'imports'

urlpatterns = [
    path('', views.home, name='home')
]
