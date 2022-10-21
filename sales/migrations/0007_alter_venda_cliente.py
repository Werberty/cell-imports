# Generated by Django 4.0.6 on 2022-10-21 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_alter_cliente_telefone'),
        ('sales', '0006_alter_venda_cliente_alter_venda_produto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendas', to='clients.cliente'),
        ),
    ]
