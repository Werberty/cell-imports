import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm

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

        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')  # noqa: E501
        if not bool(re.fullmatch(regex, email)):
            raise ValidationError('Email inválido!')

        return email
