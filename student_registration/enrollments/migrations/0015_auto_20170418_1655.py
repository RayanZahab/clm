# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-18 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0014_auto_20170319_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ndshift_school', to='schools.School'),
        ),
    ]