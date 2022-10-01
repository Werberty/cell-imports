import re

from django.core.exceptions import ValidationError
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

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['telefone'].widget.attrs.update(
            {'class': 'mask-telefone'})

    def clean_email(self):
        email = self.cleaned_data["email"]
        pather = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not bool(re.search(pather, email)):
            raise ValidationError('Email inválido!')
        return email
