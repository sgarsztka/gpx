from django.db import models
from django.utils.timezone import now
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField

# Create your models here.


class Entry(models.Model):
    entryId = models.AutoField(primary_key=True)
    entryTitle = models.CharField(max_length=155)
    entryRideDate = models.DateTimeField('Time of ride')
    entryPublicDate = models.DateTimeField('Date published')
    entryDist = models.DecimalField(max_digits=6, decimal_places=2)
    entryAvgSpeed = models.IntegerField(default=0)
    entryDescription = models.CharField(max_length=300)
    entryCadence = models.IntegerField(default=0)
    entryHeartRate = models.IntegerField(default=0)

    class Meta:
       managed = True


class GpxTrack(models.Model):
    gpxId = models.AutoField(primary_key=True)
    gpxUuid = models.CharField(max_length=100, default=0)
    gpxTitle = models.CharField(max_length=100)
    gpxUploadedDate = models.DateTimeField(default=now, editable = False)
    gpxAuthor = models.CharField(max_length=30, default='default', editable = False)
    gpxRideDate = models.DateTimeField(default=now)
    gpxDist = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    gpxAvgSpeed = models.IntegerField(default=0)
    gpxCadence = models.IntegerField(default=0)
    gpxHeartRate = models.IntegerField(default=0)
    gpxLatLonArray = JSONField(default=list)
    gpxTimesArray = ArrayField(
        models.CharField(max_length=20, blank=True),
    )
    gpxElevationArray = ArrayField(
        models.CharField(max_length=10, blank=True),
    )
    gpxAuthor = models.CharField(max_length=50, default = 'default')
    class Meta:
       managed = True

#sbl@sbl-VirtualBox:~/DjangoCode/gpx$ python3 manage.py migrate --fake gpxster zero
#python3 manage.py migrate gpxster
# or
# DROP TABLES from psql and then
# sbl@sbl-VirtualBox:~/DjangoCode/gpx$ python3 manage.py migrate --run-syncdb
