# Generated by Django 4.0.6 on 2022-10-01 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='valor_venda',
            field=models.FloatField(verbose_name='Valor da venda'),
        ),
    ]
