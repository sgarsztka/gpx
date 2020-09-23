from django.db import models

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
    entryGpx = models.ForeignKey(Entry, on_delete=models.CASCADE)

#class Map(models.Model): placeholder
