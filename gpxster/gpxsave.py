import time
import os
from django.conf import settings
from xml.dom.minidom import parse, parseString

def handle_uploaded_file(f):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    base_dir =settings.MEDIA_ROOT
    filename = os.path.join(base_dir, str(timestr)+str('.gpx'))

    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    dom1 = parse(filename)


    points = dom1.getElementsByTagName("trkpt")
    for point in points:
        lat = point.getAttribute("lat")
        lon = point.getAttribute("lon")
        elevation = point.getElementsByTagName("ele")[0]
        times = point.getElementsByTagName("time")[0]
        print("lat:%s, lon:%s , ele:%s, time:%s" %
              (lat, lon, elevation.firstChild.data, times.firstChild.data))
    os.remove(filename)
