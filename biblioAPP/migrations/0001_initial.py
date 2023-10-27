# Generated by Django 4.2.6 on 2023-10-27 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Genero',
            },
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('qtd_paginas', models.IntegerField()),
                ('qtd_livros', models.IntegerField()),
                ('imagem', models.ImageField(upload_to='')),
                ('autor', models.TextField()),
                ('created_at', models.DateField()),
                ('in_stock', models.BooleanField(default=False)),
                ('genero', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='biblioAPP.genero')),
            ],
            options={
                'verbose_name': 'Livros',
                'verbose_name_plural': 'Livros',
            },
        ),
    ]
