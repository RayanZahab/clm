# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-20 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0026_auto_20170809_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'ID Type',
            },
        ),
        migrations.RemoveField(
            model_name='idtype',
            name='inuse',
        ),
        migrations.AddField(
            model_name='student',
            name='family_status',
            field=models.CharField(blank=True, choices=[('married', 'Married'), ('engaged', 'Engaged'), ('divorced', 'Divorced'), ('widower', 'Widower'), ('single', 'Single')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='have_children',
            field=models.CharField(blank=True, choices=[(1, '\u0646\u0639\u0645'), (0, '\u0643\u0644\u0627')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='p_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
