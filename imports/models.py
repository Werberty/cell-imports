from django.db import models
from pyexpat import model


class Produto(models.Model):
    modelo = models.CharField(max_length=65)
    cor = models.CharField(max_length=35)
    memoria = models.CharField(max_length=10)
    armazenamento = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.modelo
