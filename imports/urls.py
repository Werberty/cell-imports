from django.urls import path

from . import views

app_name = 'imports'

urlpatterns = [
    path('products/', views.products, name='products'),
]
