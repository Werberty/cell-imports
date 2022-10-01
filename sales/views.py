from multiprocessing import context

from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render
from products.models import Produto

from sales.forms import VendasForm
from sales.models import Venda


def sales(request):
    if request.method == 'GET':
        form = VendasForm()
        vendas = Venda.objects.all().order_by('-id')
        context = {'form': form, 'vendas': vendas}

        return render(request,  'sales/sales.html', context)
    elif request.method == 'POST':
        form = VendasForm(request.POST)

        if form.is_valid():
            form_venda = form.save(commit=False)
            form_venda.vendedor = request.user

            form_venda.save()
            messages.add_message(
                request, constants.SUCCESS, 'Venda cadastrada')
        else:
            messages.add_message(request, constants.ERROR, 'Erro ao cadastrar')
            form = VendasForm(request.POST)
            vendas = Venda.objects.all().order_by('-id')
            context = {'form': form, 'vendas': vendas}

            return render(request, 'sales/sales.html', context)

        produto = Produto.objects.get(id=request.POST.get('produto'))
        produto.vendido = True
        produto.save()

        form = VendasForm()
        vendas = Venda.objects.all().order_by('-id')
        context = {'form': form, 'vendas': vendas}

        return render(request, 'sales/sales.html', context)
