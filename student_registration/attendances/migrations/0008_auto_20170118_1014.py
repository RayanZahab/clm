# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-18 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0007_absentee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='byschoolbyday',
            old_name='validated',
            new_name='validation_status',
        ),
        migrations.AddField(
            model_name='byschoolbyday',
            name='highest_attendance_rate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='byschoolbyday',
            name='total_absent_female',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='byschoolbyday',
            name='total_absent_male',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='byschoolbyday',
            name='total_attended_female',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='byschoolbyday',
            name='total_attended_male',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]