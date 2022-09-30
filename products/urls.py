from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('products/delete/<int:product_id>',
         views.delete_product, name='delete_product'),
    path('products/edit/<int:product_id>',
         views.edit_product, name='edit_product'),
    path('products/detail/<int:product_id>',
         views.detail_product, name='detail_product'),
]
