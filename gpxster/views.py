from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from gpxster.models import Entry, GpxTrack
from django.contrib.auth.decorators import login_required
from gpxster.forms import EntryForm, UploadGpxForm
from gpxster.gpxsave import handle_uploaded_file
import json

class Login(View):
    template = 'login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request,self.template,{'form':form})


    def post(self,request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            return render(request,self.template,{'form':form})



class Index(LoginRequiredMixin, View):
    template = 'index.html'
    login_url = '/login/'

    def get(self, request):
        username = None
        if request.user:
            username = request.user.username
        output = Entry.objects.order_by('-entryRideDate')[:10]
        tracks = GpxTrack.objects.filter(gpxAuthor=username).order_by('-gpxRideDate')[:10]
        return render(request, self.template, {'tracks' : tracks})
                                                # {'tracks' : tracks})

class AddEntry(LoginRequiredMixin, View):
    template = 'addentry.html'
    redirect_field_name = 'login'

    def get(self, request):
        form = EntryForm()
        return render(request,self.template, {'form':form})

    def post(self,request):
        if request.method == 'POST':
            form = EntryForm(request.POST)
            if form.is_valid():
                entryTitle = form.cleaned_data['title']
                entryRideDate = form.cleaned_data['rideDate']
                entryPublicDate = form.cleaned_data['publicDate']
                entryDist = form.cleaned_data['dist']
                entryAvgSpeed = form.cleaned_data['avgSpeed']
                entryDescription = form.cleaned_data['description']
                entryCadence = form.cleaned_data['cadence']
                entryHeartRate = form.cleaned_data['heartRate']
                e = Entry(entryTitle=entryTitle, entryRideDate=entryRideDate, entryPublicDate=entryPublicDate, entryDist=entryDist,
                    entryAvgSpeed=entryAvgSpeed,entryDescription=entryDescription,entryCadence=entryCadence,entryHeartRate=entryHeartRate)
                e.save()
                return HttpResponseRedirect('/')
            else:
                form = EntryForm()
            return render(request,self.template, {'form':form})


class AddGpx(LoginRequiredMixin, View):
    template = 'gpx.html'
    redirect_field_name = 'login'

    def get(self, request):
        form = UploadGpxForm()
        return render (request,self.template,{'form':form})

    def post(self, request):
        json_str = None
        username = None
        if request.user:
            username = request.user.username
        if request.method == 'POST':
            form = UploadGpxForm(request.POST, request.FILES)
            gpx = GpxTrack()
            if form.is_valid():
                json_cords, json_times, json_elevations = handle_uploaded_file(request.FILES['fileField'], username)
                json_cords_deserialized = json.loads(json_cords)
                json_times_deserialized = json.loads(json_times)
                json_elevations_deserialized = json.loads(json_elevations)


                gpx.gpxLatLonArray = json_cords_deserialized
                gpx.gpxTimesArray = json_times_deserialized
                gpx.gpxElevationArray = json_elevations_deserialized
                gpx.gpxAuthor = username
                gpx.gpxRideDate = json_times_deserialized[0]
                gpx.save()


                return HttpResponseRedirect('/gpx/')

        else:
            form = UploadGpxForm()
        return render(request, self.template, {'form': form})
