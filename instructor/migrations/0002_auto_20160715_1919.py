# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-15 19:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mcq_question',
            old_name='topicTag',
            new_name='courseTopic',
        ),
    ]
