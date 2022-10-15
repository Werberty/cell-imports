from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from products.models import Produto

from sales.forms import VendasForm
from sales.models import Venda


def sales(request):
    # if request.method == 'GET':
    sales_form_data = request.session.get('sales_form_data') or None
    form = VendasForm(sales_form_data)
    vendas = Venda.objects.all().order_by('-id')
    context = {'form': form, 'vendas': vendas}

    return render(request,  'sales/sales.html', context)
    # elif request.method == 'POST':
    #     form = VendasForm(request.POST)

    #     if form.is_valid():
    #         form_venda = form.save(commit=False)
    #         form_venda.vendedor = request.user

    #         form_venda.save()
    #         messages.add_message(
    #             request, constants.SUCCESS, 'Venda cadastrada')
    #     else:
    #         messages.add_message(request, constants.ERROR, 'Erro ao cadastrar')
    #         form = VendasForm(request.POST)
    #         vendas = Venda.objects.all().order_by('-id')
    #         context = {'form': form, 'vendas': vendas}

    #         return render(request, 'sales/sales.html', context)

    #     produto = Produto.objects.get(id=request.POST.get('produto'))
    #     produto.vendido = True
    #     produto.save()

    #     form = VendasForm()
    #     vendas = Venda.objects.all().order_by('-id')
    #     context = {'form': form, 'vendas': vendas}

    #     return render(request, 'sales/sales.html', context)


def create_sales(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['sales_form_data'] = POST
    form = VendasForm(POST)

    if form.is_valid():
        form_venda = form.save(commit=False)
        form_venda.vendedor = request.user

        form_venda.save()

        produto = Produto.objects.get(id=request.POST.get('produto'))
        produto.vendido = True
        produto.save()

        del(request.session['sales_form_data'])
        messages.success(request, 'Venda cadastrada')

    return redirect(reverse('sales:create_sales'))
