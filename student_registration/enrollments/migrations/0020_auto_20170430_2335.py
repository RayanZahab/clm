# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-30 20:35
from __future__ import unicode_literals

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0019_auto_20170427_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='loggingstudentmove',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='loggingstudentmove',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
    ]