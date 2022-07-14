from django.urls import path

from . import views

app_name = 'imports'

urlpatterns = [
    path('products/', views.products, name='products'),
    path('products/delete/<int:product_id>',
         views.delete_product, name='delete_product'),
    path('products/edit/<int:product_id>',
         views.edit_product, name='edit_product'),
]
