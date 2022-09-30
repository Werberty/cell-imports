from clients.models import Cliente
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render
from products.models import Produto

from sales.forms import VendasForm


def sales(request):
    if request.method == 'GET':
        produtos = Produto.objects.filter(vendido=False)
        clientes = Cliente.objects.all().order_by('-id')
        form = VendasForm()

        return render(request,  'sales/sales.html', context={
            'form': form,
            'produtos': produtos,
            'clientes': clientes,
        })
    elif request.method == 'POST':
        form = VendasForm(request.POST)

        if form.is_valid():
            form_venda = form.save(commit=False)
            form_venda.vendedor = request.user
            # produto = Produto.objects.get(instanse=form_venda.produto)
            # produto.status = 'VD'
            form_venda.save()
            messages.add_message(
                request, constants.SUCCESS, 'Venda cadastrada')
        else:
            messages.add_message(request, constants.ERROR, 'Erro ao cadastrar')

        form = VendasForm()
        produtos = Produto.objects.filter(vendido=False)
        clientes = Cliente.objects.all().order_by('-id')

        return render(request, 'sales/sales.html', context={
            'form': form,
            'produtos': produtos,
            'clientes': clientes,
        })
