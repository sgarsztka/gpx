# Generated by Django 3.1.1 on 2020-10-06 20:13

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('entryId', models.AutoField(primary_key=True, serialize=False)),
                ('entryTitle', models.CharField(max_length=155)),
                ('entryRideDate', models.DateTimeField(verbose_name='Time of ride')),
                ('entryPublicDate', models.DateTimeField(verbose_name='Date published')),
                ('entryDist', models.DecimalField(decimal_places=2, max_digits=6)),
                ('entryAvgSpeed', models.IntegerField(default=0)),
                ('entryDescription', models.CharField(max_length=300)),
                ('entryCadence', models.IntegerField(default=0)),
                ('entryHeartRate', models.IntegerField(default=0)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GpxTrack',
            fields=[
                ('gpxId', models.AutoField(primary_key=True, serialize=False)),
                ('gpxTitle', models.CharField(max_length=100)),
                ('gpxUploadedDate', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('gpxRideDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('gpxDist', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('gpxAvgSpeed', models.IntegerField(default=0)),
                ('gpxCadence', models.IntegerField(default=0)),
                ('gpxHeartRate', models.IntegerField(default=0)),
                ('gpxLatLonArray', models.JSONField(default=list)),
                ('gpxTimesArray', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), size=None)),
                ('gpxElevationArray', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=None)),
                ('gpxAuthor', models.CharField(default='default', max_length=50)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
