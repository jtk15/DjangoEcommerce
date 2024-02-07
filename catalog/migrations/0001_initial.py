# Generated by Django 5.0.1 on 2024-02-07 03:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=100, verbose_name='Idnetificaodr')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Descrição')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Croado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modifica em')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.category', verbose_name='categoria')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['name'],
            },
        ),
    ]
