# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-12 19:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0008_auto_20161207_1610'),
        ('attendances', '0004_auto_20161121_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='BySchoolByDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('total_enrolled', models.IntegerField(blank=True, null=True)),
                ('total_attended', models.IntegerField(blank=True, null=True)),
                ('total_absences', models.IntegerField(blank=True, null=True)),
                ('validated', models.BooleanField(default=False)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.School')),
            ],
        ),
    ]
