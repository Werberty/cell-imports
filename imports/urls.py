from django.urls import path

from . import views

app_name = 'imports'

urlpatterns = [
    path('products/', views.products, name='products'),
    path('delete_product/<int:product_id>',
         views.delete_product, name='delete_product'),
]
