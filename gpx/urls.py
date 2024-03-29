"""gpx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from gpxster import views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static

urlpatterns = [
    # path('', include('gpxster.urls')),
    path('login/',views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),
    path('add/', views.AddEntry.as_view(), name='addentry'),
    path('gpx/', views.AddGpx.as_view(), name='gpx'),
    path('gpxDetails/<uuid:gpxUuid>/', views.GpxDetails.as_view(), name='gpxDetails'),
    path('map/', views.Map.as_view(), name='map')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
