from clients.models import Clientes
from django.contrib.auth.models import User
from django.db import models
from products.models import Produto


class Vendas(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    saled_at = models.DateTimeField(auto_now_add=True)
