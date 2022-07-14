from operator import contains

from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)

from .forms import ProdutoForm
from .models import Produto


def products(request):
    if request.method == 'GET':
        produtos = Produto.objects.all().order_by('-id')
        form = ProdutoForm()
        return render(request, 'imports/products.html', context={
            'produtos': produtos,
            'form': form,
        })

    elif request.method == 'POST':
        form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(
                request, constants.SUCCESS, 'Produto cadastrado')
        else:
            messages.add_message(request, constants.ERROR, 'Erro ao cadastrar')

        produtos = Produto.objects.all().order_by('-id')
        form = ProdutoForm()

        return render(request, 'imports/products.html', context={
            'produtos': produtos,
            'form': form,
        })


def delete_product(request, product_id):
    product = Produto.objects.filter(id=product_id)

    if request.method == 'GET':
        return redirect('/products')

    if request.method == 'POST':
        product.delete()
        messages.add_message(request, constants.WARNING, 'Produto deletado')
        return redirect('/products')


def edit_product(request, product_id):
    return redirect('/products')
