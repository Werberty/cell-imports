from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Venda


class VendasForm(ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['observacoes'].widget.attrs.update(
            {'style': 'height: 70px;'})

    class Meta:
        model = Venda
        fields = [
            'cliente',
            'produto',
            'valor_venda',
            'forma_pagamento',
            'observacoes',
        ]
        labels = {
            'cliente': 'Cliente',
            'produto': 'Produto',
            'valor_venda': 'Valor da venda',
            'forma_pagamento': 'Forma de pagamento',
            'observacoes': 'Observações',
        }

    def clean_valor_venda(self):
        valor_venda = self.cleaned_data["valor_venda"]
        if valor_venda < 1000:
            raise ValidationError('Muito barato!')
        else:
            return valor_venda
