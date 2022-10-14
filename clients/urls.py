from django.urls import path

from . import views

app_name = 'clients'

urlpatterns = [
    path('clients/', views.clients, name='clients'),
    path('clients/create/', views.create_client, name='create_client'),
    path('clients/edit/<int:id_client>',
         views.edit_client, name='edit_client'),
    path('clients/delete/<int:id_client>',
         views.delete_client, name='delete_client'),
    path('clients/detail/<int:id_client>',
         views.detail_client, name='detail_client'),
]
