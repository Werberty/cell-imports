import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Produto


class ProdutoForm(forms.ModelForm):
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

        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'cor': 'Cor',
            'memoria': 'Memória',
            'armazenamento': 'Armazenamento',
            'codigo_produto': 'Código do produto',
            'valor_compra': 'Valor da compra (R$)',
        }

        widgets = {
            'marca': forms.TextInput(attrs={
                'placeholder': 'Marca do celular'
            }),
            'modelo': forms.TextInput(attrs={
                'placeholder': 'Modelo do celular'
            }),
            'codigo_produto': forms.TextInput(attrs={
                'placeholder': 'Ex.: 1A2C3V'
            }),
            'cor': forms.TextInput(attrs={
                'placeholder': 'Nome da cor'
            }),
        }

    def clean_codigo_produto(self):
        codigo = self.cleaned_data.get('codigo_produto', '')

        if not (len(codigo.strip()) > 0):
            raise ValidationError('String vázia!')
        elif not bool(re.match('^[A-Za-z0-9_-]*$', codigo)):
            raise ValidationError('Somente letras e números!')

        return codigo.upper()
