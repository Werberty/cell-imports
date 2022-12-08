from django import forms

from products.models import Produto

from .models import Venda


class VendasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['observacoes'].widget.attrs.update(
            {'style': 'height: 70px;'})

    produto = forms.ModelChoiceField(
        label='Produto',
        queryset=Produto.objects.filter(vendido=False)
    )

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
            'valor_venda': 'Valor da venda (R$)',
            'forma_pagamento': 'Forma de pagamento',
            'observacoes': 'Observações',
        }
