from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from gpxster.models import Entry

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
        # latestEntriesList = Entry.objects.order_by('-entryRideDate')[:10]
        output = Entry.objects.order_by('-entryRideDate')[:10]
        # output = ','.join([q.entryTitle for q in latestEntriesList])
        print(output)
        return render(request, self.template, {'output': output})
