# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-26 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0002_auto_20161025_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='last_informal_edu_final_result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.ClassLevel'),
        ),
    ]
