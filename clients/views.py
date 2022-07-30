from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render

from .forms import ClientesForm


def clients(request):
    if request.method == 'GET':
        form = ClientesForm()
        return render(request, 'clients.html', context={
            'form': form
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
        return render(request, 'clients.html', context={
            'form': form
        })
