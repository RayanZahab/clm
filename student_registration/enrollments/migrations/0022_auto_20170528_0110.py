# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-27 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0021_auto_20170525_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='exam_result_artistic',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Artistic field'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='exam_result_linguistic',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Linguistic field'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='exam_result_mathematics',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Scientific domain/Mathematics'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='exam_result_physical',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Physical field'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='exam_result_sciences',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Scientific domain/Sciences'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='exam_result_sociology',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Sociology field'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='exam_result',
            field=models.CharField(blank=True, choices=[('graduated', '\u0646\u0627\u062c\u062d/\u0629'), ('failed', '\u0645\u0639\u064a\u062f/\u0629')], max_length=50, null=True, verbose_name='\u0648\u0636\u0639 \u0627\u0644\u062a\u0644\u0645\u064a\u0630'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='exam_result_bio',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='\u0639\u0644\u0648\u0645 \u0627\u0644\u062d\u064a\u0627\u0629'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='exam_result_chemistry',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='\u0643\u064a\u0645\u064a\u0627\u0621'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='exam_result_education',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='\u062a\u0631\u0628\u064a\u0629'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='exam_result_geo',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='\u062c\u063a\u0631\u0627\u0641\u064a\u0627'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='exam_result_physic',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='\u0641\u064a\u0632\u064a\u0627\u0621'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='exam_total',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='\u0627\u0644\u0639\u0644\u0627\u0645\u0629 \u0627\u0644\u0646\u0647\u0627\u0626\u064a\u0629'),
        ),
    ]
