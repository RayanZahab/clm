# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-21 07:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_auto_20161020_1312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classlevel',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='educationlevel',
            options={'ordering': ['id']},
        ),
    ]