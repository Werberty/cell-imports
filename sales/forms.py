from dataclasses import field

from django.forms import ModelForm

from .models import Venda


class VendasForm(ModelForm):
    class Meta:
        model = Venda
        fields = [
            'cliente',
            'produto',
            'valor_venda',
        ]
