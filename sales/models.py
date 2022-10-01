from clients.models import Cliente
from django.contrib.auth.models import User
from django.db import models
from products.models import Produto


class Venda(models.Model):
    vendedor = models.ForeignKey(
        User, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.DO_NOTHING)
    produto = models.OneToOneField(
        Produto, on_delete=models.DO_NOTHING)
    valor_venda = models.FloatField(verbose_name='Valor da venda')
    saled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.produto.marca} {self.produto.modelo}'
