# Generated by Django 4.0.6 on 2022-07-13 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='armazenamento',
            field=models.IntegerField(choices=[(32, '32Gb RAM'), (64, '64Gb RAM'), (
                128, '128Gb RAM'), (256, '256Gb RAM'), (512, '512Gb RAM')]),
        ),
        migrations.AlterField(
            model_name='produto',
            name='memoria',
            field=models.IntegerField(choices=[(
                2, '2Gb RAM'), (4, '4Gb RAM'), (6, '6Gb RAM'), (8, '8Gb RAM'), (12, '12Gb RAM')]),
        ),
    ]
