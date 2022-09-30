from email.policy import default

from django.db import models


class Produto(models.Model):
    MEMORIA_CHOICES = (
        (2, '2Gb RAM'),
        (4, '4Gb RAM'),
        (6, '6Gb RAM'),
        (8, '8Gb RAM'),
        (12, '12Gb RAM'),
    )

    ARMAZ_CHOICES = (
        (16, '16Gb ROM'),
        (32, '32Gb ROM'),
        (64, '64Gb ROM'),
        (128, '128Gb ROM'),
        (256, '256Gb ROM'),
        (512, '512Gb ROM'),
    )

    STATUS_CHOICES = (
        ('ET', 'Estoque'),
        ('VD', 'Vendido'),
    )

    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=65)
    cor = models.CharField(max_length=35)
    memoria = models.IntegerField(choices=MEMORIA_CHOICES)
    armazenamento = models.IntegerField(choices=ARMAZ_CHOICES)
    codigo_produto = models.CharField(max_length=65, blank=True)
    valor_compra = models.FloatField()
    vendido = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.marca} {self.modelo}'
