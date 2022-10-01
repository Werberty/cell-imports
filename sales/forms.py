from django.core.exceptions import ValidationError
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

    def clean_valor_venda(self):
        valor_venda = self.cleaned_data["valor_venda"]
        if valor_venda < 1000:
            raise ValidationError('Muito barato!')
        else:
            return valor_venda
