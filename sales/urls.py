from django.urls import path

from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.sales, name='sales'),
    path('create/', views.create_sales, name='create_sales'),
]
