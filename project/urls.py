from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stock/', include('products.urls')),
    path('', include('clients.urls')),
    path('auth/', include('authentication.urls')),
    path('sales/', include('sales.urls')),
]
