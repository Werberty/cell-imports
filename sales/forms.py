from django import forms
from django.core.exceptions import ValidationError

from products.models import Produto

from .models import Venda

produtos = Produto.objects.filter(vendido=False)


def queryset_to_tuple_list(queryset):
    result = []
    for query in queryset.values():
        result.append(
            ((query['id']), (f"{query['marca']} {query['modelo']}"))
        )
    return result


class VendasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['observacoes'].widget.attrs.update(
            {'style': 'height: 70px;'})

    produto = forms.ChoiceField(choices=queryset_to_tuple_list(produtos))

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
