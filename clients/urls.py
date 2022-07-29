from django.urls import path

from . import views

app_name = 'clients'

urlpatterns = [
    path('clients/', views.clients, name='clients')
]
