# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-31 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0002_auto_20160715_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcq_question',
            name='choiceA',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mcq_question',
            name='choiceB',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mcq_question',
            name='choiceC',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mcq_question',
            name='choiceD',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mcq_question',
            name='choiceE',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mcq_question',
            name='choiceF',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]