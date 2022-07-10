from django.http import HttpResponse
from django.shortcuts import render


def products(request):
    if request.method == 'GET':
        return render(request, 'imports/products.html')
