from django.db import models
from django.utils.timezone import now
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Entry(models.Model):
    entryTitle = models.CharField(max_length=155)
    entryRideDate = models.DateTimeField('Time of ride')
    entryPublicDate = models.DateTimeField('Date published')
    entryDist = models.DecimalField(max_digits=6, decimal_places=2)
    entryAvgSpeed = models.IntegerField(default=0)
    entryDescription = models.CharField(max_length=300)
    entryCadence = models.IntegerField(default=0)
    entryHeartRate = models.IntegerField(default=0)



class GpxTrack(models.Model):
    gpxTitle = models.CharField(max_length=100, default='Ride')
    gpxUploadedDate = models.DateTimeField(default=now, editable = False)
    gpxAuthor = models.CharField(max_length=30, default='default', editable = False)
    gpxRideDate = models.DateTimeField(default=now)
    gpxDist = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    gpxAvgSpeed = models.IntegerField(default=0)
    gpxCadence = models.IntegerField(default=0)
    gpxHeartRate = models.IntegerField(default=0)
