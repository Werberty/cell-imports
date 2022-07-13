from django.db import models
from pyexpat import model


class Produto(models.Model):
    MEMORIA_CHOICES = (
        (2, '2Gb RAM'),
        (4, '4Gb RAM'),
        (6, '6Gb RAM'),
        (8, '8Gb RAM'),
        (12, '12Gb RAM'),
    )

    ARMAZ_CHOICES = (
        (32, '32Gb RAM'),
        (64, '64Gb RAM'),
        (128, '128Gb RAM'),
        (256, '256Gb RAM'),
        (512, '512Gb RAM'),
    )

    modelo = models.CharField(max_length=65)
    cor = models.CharField(max_length=35)
    memoria = models.IntegerField(choices=MEMORIA_CHOICES)
    armazenamento = models.IntegerField(choices=ARMAZ_CHOICES)

    def __str__(self) -> str:
        return self.modelo
