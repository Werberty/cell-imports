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
        ]
