from django.contrib import admin
from .models import Entry, GpxTrack

# Register your models here.

admin.site.register(Entry)
admin.site.register(GpxTrack)
