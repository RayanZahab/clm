# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-20 10:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classroom',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['id']},
        ),
    ]