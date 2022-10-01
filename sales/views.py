from clients.models import Cliente
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render
from products.models import Produto

from sales.forms import VendasForm


def sales(request):
    if request.method == 'GET':
        form = VendasForm()

        return render(request,  'sales/sales.html', context={
            'form': form,
        })
    elif request.method == 'POST':
        form = VendasForm(request.POST)

        if form.is_valid():
            form_venda = form.save(commit=False)
            form_venda.vendedor = request.user
            # form_venda.produto.vendido = True

            produto = Produto.objects.filter(id=form_venda.produto.id)
            produto.vendido = True

            form_venda.save()
            messages.add_message(
                request, constants.SUCCESS, 'Venda cadastrada')
        else:
            messages.add_message(request, constants.ERROR, 'Erro ao cadastrar')
            form = VendasForm(request.POST)

            return render(request, 'sales/sales.html', context={
                'form': form,
            })

        form = VendasForm()

        return render(request, 'sales/sales.html', context={
            'form': form,
        })
