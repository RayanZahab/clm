# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-15 16:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_schools'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='app_password',
        ),
    ]