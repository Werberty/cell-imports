# Generated by Django 4.0.6 on 2022-10-15 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_venda_forma_pagamento_venda_observacoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='forma_pagamento',
            field=models.CharField(blank=True, choices=[('DN', 'Dinheiro'), ('PX', 'PIX'), ('CC', 'Cartão de crédito'), ('CD', 'Cartão de débito'), ('OT', 'Outros')], default='OT', max_length=2),
        ),
    ]