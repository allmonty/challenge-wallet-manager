# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 21:44
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20171117_0335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcard',
            name='avilable_amount',
        ),
        migrations.AddField(
            model_name='creditcard',
            name='available_amount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20, verbose_name='Available Amount'),
        ),
        migrations.AddField(
            model_name='wallet',
            name='limit',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20, verbose_name='Limit'),
        ),
        migrations.AddField(
            model_name='wallet',
            name='owner_email',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='Owner Email'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='limit',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20, verbose_name='Limit'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='owner_name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Owner Name'),
        ),
    ]