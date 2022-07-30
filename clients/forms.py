from django.forms import ModelForm
from pyexpat import model

from .models import Clientes


class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        fields = [
            'nome',
            'sobrenome',
            'telefone',
            'email',
        ]
