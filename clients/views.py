from ast import Return

from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import get_object_or_404, render

from .forms import ClientesForm
from .models import Clientes


def clients(request):
    if request.method == 'GET':
        clientes = Clientes.objects.filter(vendedor=request.user)
        form = ClientesForm()
        return render(request, 'clients/clients.html', context={
            'form': form,
            'clientes': clientes,
        })
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form_client = form.save(commit=False)
            form_client.vendedor = request.user
            form_client.save()
            messages.add_message(
                request, constants.SUCCESS, 'Cliente cadastrado')
        else:
            messages.add_message(request, constants.ERROR, 'Erro ao cadastrar')

        form = ClientesForm()
        return render(request, 'clients/clients.html', context={
            'form': form
        })


def edit_client(request, id_client):
    cliente = get_object_or_404(Clientes, id=id_client)
    clientes = Clientes.objects.filter(vendedor=request.user).order_by('-id')
    form = ClientesForm(instance=cliente)
    if request.method == 'GET':
        return render(request, 'clients/edit_client.html', context={
            'cliente': cliente,
            'clientes': clientes,
            'form': form,
        })
    if request.method == 'POST':
        form = ClientesForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            messages.add_message(
                request, constants.SUCCESS, 'Cliente editado')
        else:
            messages.add_message(request, constants.ERROR, 'Erro ao editar')

        form = ClientesForm()

        return render(request, 'clients/clients.html', context={
            'cliente': cliente,
            'clientes': clientes,
            'form': form,
        })
