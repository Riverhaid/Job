# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170327_1957'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='category',
            name='nameCategory',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='polls.Category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.RemoveField(
            model_name='product',
            name='CategoryID',
        ),
        migrations.RemoveField(
            model_name='product',
            name='ColorProduct',
        ),
        migrations.RemoveField(
            model_name='product',
            name='DescriptionProduct',
        ),
        migrations.RemoveField(
            model_name='product',
            name='NameProduct',
        ),
        migrations.RemoveField(
            model_name='product',
            name='PriceProduct',
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
