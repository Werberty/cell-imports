# Generated by Django 4.0.6 on 2022-10-21 00:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_alter_cliente_telefone'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0004_alter_produto_codigo_produto_and_more'),
        ('sales', '0005_alter_venda_forma_pagamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendas', to='clients.cliente'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='produto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vendas', to='products.produto'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendas', to=settings.AUTH_USER_MODEL),
        ),
    ]
