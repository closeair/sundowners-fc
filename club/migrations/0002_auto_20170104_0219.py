# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-04 02:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyquestion',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='surveyresponse',
            name='approve',
        ),
        migrations.RemoveField(
            model_name='surveyresponse',
            name='question',
        ),
        migrations.DeleteModel(
            name='SurveyQuestion',
        ),
    ]
