# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-31 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20161002_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='pilot_in_use',
            field=models.BooleanField(default=False),
        ),
    ]
