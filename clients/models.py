from django.contrib.auth.models import User
from django.db import models
from django.forms import model_to_dict


class Clientes(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=65)
    sobrenome = models.CharField(max_length=256)
    telefone = models.CharField(max_length=18)
    email = models.EmailField(max_length=256)

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'
