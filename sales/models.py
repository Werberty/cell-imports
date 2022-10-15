from clients.models import Cliente
from django.contrib.auth.models import User
from django.db import models
from products.models import Produto


class Venda(models.Model):
    CHOICES_PAGAMENTO = (
        ('DN', 'Dinheiro'),
        ('PX', 'PIX'),
        ('CC', 'Cartão de crédito'),
        ('CD', 'Cartão de débito'),
        ('OT', 'Outros'),
    )

    vendedor = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='vendas')
    cliente = models.ForeignKey(
        Cliente, on_delete=models.DO_NOTHING, related_name='vendas')
    produto = models.OneToOneField(
        Produto, on_delete=models.DO_NOTHING, related_name='vendas')
    valor_venda = models.FloatField(verbose_name='Valor da venda')
    forma_pagamento = models.CharField(
        max_length=2, choices=CHOICES_PAGAMENTO, blank=True, default='OT')
    observacoes = models.TextField(blank=True, default='Nenhuma')
    saled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.produto.marca} {self.produto.modelo}'
