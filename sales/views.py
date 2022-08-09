from django.shortcuts import render

from .forms import VendasForm


def sales(request):
    form = VendasForm()
    return render(request,  'sales/sales.html', context={
        'form': form,
    })
