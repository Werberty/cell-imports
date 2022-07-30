from django.urls import path

from . import views

app_name = 'clients'

urlpatterns = [
    path('clients/', views.clients, name='clients'),
    path('clients/edit/<int:id_client>', views.edit_client, name='edit_client')
]
