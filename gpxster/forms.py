from django import forms
import datetime

class EntryForm(forms.Form):
    title = forms.CharField(max_length=155)
    rideDate = forms.DateTimeField(initial=datetime.date.today)
    publicDate = forms.DateTimeField(initial=datetime.date.today)
    dist = forms.DecimalField(max_digits=6, decimal_places=2)
    avgSpeed = forms.IntegerField()
    description = forms.CharField(max_length=300)
    cadence = forms.IntegerField()
    heartRate = forms.IntegerField()
