# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-04 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0002_auto_20161023_0537'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aircraft',
            options={'verbose_name_plural': 'Aircraft'},
        ),
        migrations.AddField(
            model_name='flight',
            name='starting_hobbs',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='starting_tach',
            field=models.FloatField(null=True),
        ),
    ]
