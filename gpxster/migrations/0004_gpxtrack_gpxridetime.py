# Generated by Django 3.1.1 on 2021-02-12 23:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gpxster', '0003_auto_20210212_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpxtrack',
            name='gpxRideTime',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]