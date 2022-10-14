from curses.ascii import HT

from django.contrib import messages
from django.contrib.messages import constants
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from sales.models import Venda

from .forms import ClientesForm
from .models import Cliente


def clients(request):
    client_form_data = request.session.get('client_form_data') or None
    clientes = Cliente.objects.all().order_by('-id')
    form = ClientesForm(client_form_data)
    return render(request, 'clients/clients.html', context={
        'form': form,
        'clientes': clientes,
    })


def create_client(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['client_form_data'] = POST
    form = ClientesForm(POST)

    if form.is_valid():
        form_client = form.save(commit=False)
        form_client.vendedor = request.user
        form_client.save()
        del(request.session['client_form_data'])
        messages.success(request, 'Cliente cadastrado')

    return redirect(reverse('clients:clients'))


def edit_client(request, id_client):
    cliente = get_object_or_404(Cliente, id=id_client)

    if request.method == 'GET':
        clientes = Cliente.objects.all().order_by('-id')
        form = ClientesForm(instance=cliente)
        context = {'form': form, 'cliente': cliente, 'clientes': clientes}
        return render(request, 'clients/edit_client.html', context)

    elif request.method == 'POST':
        form = ClientesForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            messages.add_message(
                request, constants.SUCCESS, 'Cliente editado')
        else:
            messages.add_message(request, constants.ERROR, 'Erro ao editar')
            form = ClientesForm(request.POST)
            cliente = get_object_or_404(Cliente, id=id_client)
            clientes = Cliente.objects.all().order_by('-id')
            context = {'form': form, 'cliente': cliente,
                       'clientes': clientes}

            return render(request, 'clients/edit_client.html', context)

        form = ClientesForm()
        clientes = Cliente.objects.all().order_by('-id')
        context = {'clientes': clientes, 'form': form}

        return render(request, 'clients/clients.html', context)


def delete_client(request, id_client):
    cliente = Cliente.objects.filter(id=id_client)
    if request.method == 'GET':
        return redirect(reverse('clients:clients'))
    if request.method == 'POST':
        cliente.delete()
        messages.add_message(request, constants.WARNING, 'Cliente deletado')
        return redirect(reverse('clients:clients'))


def detail_client(request, id_client):
    cliente = get_object_or_404(Cliente, id=id_client)
    compras = Venda.objects.filter(cliente__id=id_client)

    return render(request, 'clients/detail_client.html', context={
        'cliente': cliente,
        'compras': compras,
    })
