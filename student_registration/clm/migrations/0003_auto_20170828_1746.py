# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-28 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0005_auto_20170731_2134'),
        ('clm', '0002_auto_20170828_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='bln',
            name='governorate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='locations.Location'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='governorate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='locations.Location'),
        ),
        migrations.AddField(
            model_name='rs',
            name='governorate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='locations.Location'),
        ),
    ]
