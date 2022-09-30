from django.forms import ModelForm
from pyexpat import model

from .models import Cliente


class ClientesForm(ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'sobrenome',
            'telefone',
            'email',
        ]
