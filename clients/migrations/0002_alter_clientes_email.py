# Generated by Django 4.0.6 on 2022-08-01 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(max_length=256),
        ),
    ]
