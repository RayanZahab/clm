# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-27 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0005_auto_20161027_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='last_school_type',
            field=models.CharField(blank=True, choices=[('out_the_country', '\u0645\u062f\u0631\u0633\u0629 \u062e\u0627\u0631\u062c \u0644\u0628\u0646\u0627\u0646'), ('public_in_country', '\u0645\u062f\u0631\u0633\u0629 \u0631\u0633\u0645\u064a\u0629 \u0641\u064a \u0644\u0628\u0646\u0627\u0646'), ('private_in_country', '\u0645\u062f\u0631\u0633\u0629 \u062e\u0627\u0635\u0629 \u0641\u064a \u0644\u0628\u0646\u0627\u0646')], max_length=50, null=True),
        ),
    ]