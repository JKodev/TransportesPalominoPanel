# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160915_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='departure_date',
            field=models.DateTimeField(verbose_name='Fecha de Salida'),
        ),
    ]