# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-20 18:01
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schools', '0019_educationallevel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0005_auto_20170731_2134'),
        ('students', '0027_auto_20170820_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('assessment_form', models.URLField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BLN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('language', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('english_arabic', 'English/Arabic'), ('french_arabic', 'French/Arabic')], max_length=50, null=True), blank=True, null=True, size=None)),
                ('have_labour', models.CharField(blank=True, choices=[(1, '\u0646\u0639\u0645'), (0, '\u0643\u0644\u0627')], max_length=50, null=True)),
                ('labour_hours', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('enrolled', 'enrolled'), ('pre_test', 'pre_test'), ('post_test', 'post_test')], default='enrolled', max_length=50)),
                ('pre_test', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('post_test', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('scores', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('dropout_status', models.BooleanField(default=False)),
                ('moved', models.BooleanField(default=False)),
                ('outreach_barcode', models.CharField(blank=True, max_length=50, null=True)),
                ('new_registry', models.CharField(blank=True, choices=[(1, '\u0646\u0639\u0645'), (0, '\u0643\u0644\u0627')], max_length=50, null=True)),
                ('student_outreached', models.CharField(blank=True, choices=[(1, '\u0646\u0639\u0645'), (0, '\u0643\u0644\u0627')], max_length=50, null=True)),
                ('have_barcode', models.CharField(blank=True, choices=[(1, '\u0646\u0639\u0645'), (0, '\u0643\u0644\u0627')], max_length=50, null=True)),
                ('registration_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CBECE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('language', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('english_arabic', 'English/Arabic'), ('french_arabic', 'French/Arabic')], max_length=50, null=True), blank=True, null=True, size=None)),
                ('have_labour', models.CharField(blank=True, choices=[(1, '\u0646\u0639\u0645'), (0, '\u0643\u0644\u0627')], max_length=50, null=True)),
                ('labour_hours', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('enrolled', 'enrolled'), ('pre_test', 'pre_test'), ('post_test', 'post_test')], default='enrolled', max_length=50)),
                ('pre_test', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('post_test', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('scores', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('dropout_status', models.BooleanField(default=False)),
                ('moved', models.BooleanField(default=False)),
                ('outreach_barcode', models.CharField(blank=True, max_length=50, null=True)),
                ('new_registry', models.CharField(blank=True, choices=[(1, '\u0646\u0639\u0645'), (0, '\u0643\u0644\u0627')], max_length=50, null=True)),
                ('student_outreached', models.CharField(blank=True, choices=[(1, '\u0646\u0639\u0645'), (0, '\u0643\u0644\u0627')], max_length=50, null=True)),
                ('have_barcode', models.CharField(blank=True, choices=[(1, '\u0646\u0639\u0645'), (0, '\u0643\u0644\u0627')], max_length=50, null=True)),
                ('registration_date', models.DateField(blank=True, null=True)),
                ('child_muac', models.CharField(blank=True, choices=[('1', '< 11.5 CM (severe malnutrition)'), ('2', '< 12.5 CM (moderate malnutrition)')], max_length=50, null=True)),
                ('pre_test_arabic', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19)], null=True)),
                ('pre_test_language', models.FloatField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19)], null=True)),
                ('pre_test_math', models.FloatField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19)], null=True)),
                ('pre_test_science', models.FloatField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19)], null=True)),
                ('school_readiness', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('current_cycle', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Disability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('language', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('english_arabic', 'English/Arabic'), ('french_arabic', 'French/Arabic')], max_length=50, null=True), blank=True, null=True, size=None)),
                ('have_labour', models.CharField(blank=True, choices=[(1, '\u0646\u0639\u0645'), (0, '\u0643\u0644\u0627')], max_length=50, null=True)),
                ('labour_hours', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('enrolled', 'enrolled'), ('pre_test', 'pre_test'), ('post_test', 'post_test')], default='enrolled', max_length=50)),
                ('pre_test', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('post_test', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('scores', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('dropout_status', models.BooleanField(default=False)),
                ('moved', models.BooleanField(default=False)),
                ('outreach_barcode', models.CharField(blank=True, max_length=50, null=True)),
                ('new_registry', models.CharField(blank=True, choices=[(1, '\u0646\u0639\u0645'), (0, '\u0643\u0644\u0627')], max_length=50, null=True)),
                ('student_outreached', models.CharField(blank=True, choices=[(1, '\u0646\u0639\u0645'), (0, '\u0643\u0644\u0627')], max_length=50, null=True)),
                ('have_barcode', models.CharField(blank=True, choices=[(1, '\u0646\u0639\u0645'), (0, '\u0643\u0644\u0627')], max_length=50, null=True)),
                ('registration_date', models.DateField(blank=True, null=True)),
                ('shift', models.CharField(blank=True, choices=[('first', '\u062f\u0648\u0627\u0645 \u0635\u0628\u0627\u062d\u064a'), ('second', '\u062f\u0648\u0627\u0645 \u0628\u0639\u062f \u0627\u0644\u0638\u0647\u0631')], max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RSCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('current_cycle', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('current_cycle', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='rs',
            name='cycle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='clm.RSCycle'),
        ),
        migrations.AddField(
            model_name='rs',
            name='disability',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='clm.Disability'),
        ),
        migrations.AddField(
            model_name='rs',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='locations.Location'),
        ),
        migrations.AddField(
            model_name='rs',
            name='hh_educational_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.EducationalLevel'),
        ),
        migrations.AddField(
            model_name='rs',
            name='labours',
            field=models.ManyToManyField(blank=True, related_name='_rs_labours_+', to='students.Labour'),
        ),
        migrations.AddField(
            model_name='rs',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rs',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.School'),
        ),
        migrations.AddField(
            model_name='rs',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='clm.Site'),
        ),
        migrations.AddField(
            model_name='rs',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='students.Student'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='cycle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='clm.Cycle'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='disability',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='clm.Disability'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='locations.Location'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.ClassRoom'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='hh_educational_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.EducationalLevel'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='labours',
            field=models.ManyToManyField(blank=True, related_name='_cbece_labours_+', to='students.Labour'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cbece',
            name='referral',
            field=models.ManyToManyField(blank=True, related_name='_cbece_referral_+', to='clm.Cycle'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='referral_reasons',
            field=models.ManyToManyField(blank=True, related_name='_cbece_referral_reasons_+', to='clm.Cycle'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.School'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='clm.Site'),
        ),
        migrations.AddField(
            model_name='cbece',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='students.Student'),
        ),
        migrations.AddField(
            model_name='bln',
            name='cycle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='clm.Cycle'),
        ),
        migrations.AddField(
            model_name='bln',
            name='disability',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='clm.Disability'),
        ),
        migrations.AddField(
            model_name='bln',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='locations.Location'),
        ),
        migrations.AddField(
            model_name='bln',
            name='hh_educational_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='schools.EducationalLevel'),
        ),
        migrations.AddField(
            model_name='bln',
            name='labours',
            field=models.ManyToManyField(blank=True, related_name='_bln_labours_+', to='students.Labour'),
        ),
        migrations.AddField(
            model_name='bln',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bln',
            name='referral',
            field=models.ManyToManyField(blank=True, related_name='_bln_referral_+', to='clm.Cycle'),
        ),
        migrations.AddField(
            model_name='bln',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='students.Student'),
        ),
    ]
