# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-01 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_student_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='number',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
