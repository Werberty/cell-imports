from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render

from .models import Produto


def products(request):
    if request.method == 'GET':
        produtos = Produto.objects.all()
        return render(request, 'imports/products.html', context={
            'produtos': produtos,
        })

    elif request.method == 'POST':
        modelo = request.POST.get('modelo')
        cor = request.POST.get('cor')
        memoria = request.POST.get('memoria')
        armazenamento = request.POST.get('armazenamento')

        produto = Produto(
            modelo=modelo,
            cor=cor,
            memoria=memoria,
            armazenamento=armazenamento
        )
        produto.save()

        messages.add_message(request, constants.SUCCESS, 'Produto cadastrado')
        return render(request, 'imports/products.html')
