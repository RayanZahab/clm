# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-15 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alp', '0020_auto_20170215_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='alpround',
            name='current_round',
            field=models.BooleanField(default=False),
        ),
    ]