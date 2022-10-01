import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Produto


class ProdutoForm(ModelForm):
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
        if not (len(codigo.strip()) > 0):
            raise ValidationError('String vázia!')
        elif not bool(re.match('^[A-Za-z0-9_-]*$', codigo)):
            raise ValidationError('Somente letras e números!')
        else:
            return codigo.upper()
