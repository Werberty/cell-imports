import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Produto


class ProdutoForm(ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['codigo_produto'].widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Produto
        fields = [
            'marca',
            'modelo',
            'cor',
            'memoria',
            'armazenamento',
            'codigo_produto',
            'valor_compra',
        ]

    def clean_codigo_produto(self):
        codigo = self.cleaned_data["codigo_produto"]
        exists = Produto.objects.filter(codigo_produto=codigo).exists()

        if exists:
            raise ValidationError(
                'Código de produto já existe',
                code='invalid'
            )

        if not (len(codigo.strip()) > 0):
            raise ValidationError('String vázia!')
        elif not bool(re.match('^[A-Za-z0-9_-]*$', codigo)):
            raise ValidationError('Somente letras e números!')

        return codigo.upper()
