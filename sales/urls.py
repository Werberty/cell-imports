from django.urls import path

from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.sales, name='sales'),
    path('nota-fiscal/view/<int:id_sale>',
         views.view_nota_fiscal, name='view_nota_fiscal'),
    path('nota-fiscal/download/<int:id_sale>',
         views.down_nota_fiscal, name='down_nota_fiscal'),
    path('create', views.create_sales, name='create_sales'),
]
