# Generated by Django 4.0.6 on 2022-07-14 19:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0006_alter_produto_vendedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='vendedor',
            field=models.ForeignKey(
                default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
