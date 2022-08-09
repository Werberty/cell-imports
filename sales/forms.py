from dataclasses import field

from django.forms import ModelForm

from .models import Vendas


class VendasForm(ModelForm):
    class Meta:
        model = Vendas
        fields = [
            'cliente',
            'produto',
        ]
