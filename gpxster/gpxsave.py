import time
import os
from django.conf import settings
from xml.dom.minidom import parse, parseString
import json
from geojson import MultiPoint

def handle_uploaded_file(f, username):
    pointsList = []
    timesList = []
    elevationList = []
    gpxList = []
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
        # tempTuple = (float(lat),float(lon),float(elevation.firstChild.data),times.firstChild.data)
        cordTuple = (float(lat),float(lon))
        pointsList.append(cordTuple)
        timesTuple = times.firstChild.data
        timesList.append(timesTuple)
        elevationTuple =(float(elevation.firstChild.data))
        elevationList.append(elevationTuple)

        # print("lat:%s, lon:%s , ele:%s, time:%s" %
        #       (lat, lon, elevation.firstChild.data, times.firstChild.data))
    # spointsList.append(username)
    gpxList.append(pointsList)
    os.remove(filename)
    a = MultiPoint(pointsList)

    # for x in range(0,len(gpxList)):
    #     print(gpxList[x])

    cord_response = json.dumps(a)
    time_response = json.dumps(timesList)
    elevation_response = json.dumps(elevationList)
    return cord_response, time_response, elevation_response
