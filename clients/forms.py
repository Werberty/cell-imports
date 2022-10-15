import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Cliente


class ClientesForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'sobrenome',
            'telefone',
            'email',
        ]

        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'telefone': 'Telefone',
            'email': 'E-mail',
        }

        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Ex.: João'
            }),
            'sobrenome': forms.TextInput(attrs={
                'placeholder': 'Ex.: Alberto de Sousa'
            }),
            'telefone': forms.TextInput(attrs={
                'placeholder': '(XX) XXXXX-XXXX'
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'exemplo@email.com'
            }),
        }

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
