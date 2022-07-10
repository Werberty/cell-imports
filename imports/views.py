from django.http import HttpResponse
from django.shortcuts import render


def produtos(request):
    return HttpResponse('Listar produtos')
