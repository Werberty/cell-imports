from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=65)
    sobrenome = models.CharField(max_length=256)
    telefone = models.CharField(max_length=18, unique=True)
    email = models.EmailField(max_length=256, unique=True)

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'
