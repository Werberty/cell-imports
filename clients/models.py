from django.contrib.auth.models import User
from django.db import models


class Clientes(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=65)
    sobrenome = models.CharField(max_length=256)
    telefone = models.CharField(max_length=18)
    email = models.CharField(max_length=65)
