from django.db import models
from django.utils.timezone import now

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
    gpxDocument = models.FileField(upload_to='gpxs/%Y/%m/%d/', blank=True)
    gpxUploadedDate = models.DateTimeField(default=now, editable = False)
#class Map(models.Model): placeholder
