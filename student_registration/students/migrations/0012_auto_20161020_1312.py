# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-20 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_student_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nationality',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='nationality',
            name='code',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
