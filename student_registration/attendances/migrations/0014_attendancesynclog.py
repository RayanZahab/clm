# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-13 08:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schools', '0010_alprefermatrix_age'),
        ('attendances', '0013_auto_20170320_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceSyncLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_records', models.IntegerField(default=0)),
                ('total_processed', models.IntegerField(default=0)),
                ('successful', models.BooleanField(default=False)),
                ('exception_message', models.TextField(blank=True, null=True)),
                ('processed_date', models.DateTimeField(auto_now=True)),
                ('processed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.School')),
            ],
            options={
                'ordering': ['processed_date'],
            },
        ),
    ]