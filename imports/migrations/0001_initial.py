# Generated by Django 4.0.6 on 2022-07-12 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=65)),
                ('cor', models.CharField(max_length=35)),
                ('memoria', models.CharField(max_length=10)),
                ('armazenamento', models.CharField(max_length=10)),
            ],
        ),
    ]
