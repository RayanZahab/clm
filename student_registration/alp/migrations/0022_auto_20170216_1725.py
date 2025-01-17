# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-16 15:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alp', '0021_alpround_current_round'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentOutreach',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('alp.outreach',),
        ),
        migrations.CreateModel(
            name='CurrentRound',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('alp.outreach',),
        ),
        migrations.CreateModel(
            name='PostTest',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('alp.outreach',),
        ),
        migrations.CreateModel(
            name='PreTest',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('alp.outreach',),
        ),
        migrations.AlterModelOptions(
            name='outreach',
            options={'ordering': ['id'], 'verbose_name': 'All ALP data'},
        ),
        migrations.RenameField(
            model_name='outreach',
            old_name='post_exam_level',
            new_name='refer_to_level',
        ),
    ]
