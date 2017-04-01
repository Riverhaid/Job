# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Color',
        ),
        migrations.AddField(
            model_name='product',
            name='ColorProduct',
            field=models.CharField(max_length=20, null=True, verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='product',
            name='DescriptionProduct',
            field=models.CharField(max_length=100, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='PriceProduct',
            field=models.CharField(max_length=20, null=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='NameProduct',
            field=models.CharField(max_length=50, null=True, verbose_name='Product'),
        ),
    ]
