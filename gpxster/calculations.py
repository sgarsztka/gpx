from geopy.distance import geodesic
from gpxster.models import Entry, GpxTrack
from datetime import datetime, timezone


def calculate_distance(distance):
    dist_points = len(distance)
    sum = 0
    for x in range(0,dist_points-1):
        b = geodesic(distance[x+1], distance[x]).kilometers
        # print("dist point", b)
        sum += b
    return sum


def calculate_time(time):
    time_length= len(time)
    time_start = datetime.strptime(time[0],"%Y-%m-%dT%H:%M:%SZ")
    # time_start = datetime.fromtimestamp(time[0], timezone.utc)
    # time_stop = datetime.fromtimestamp(time[time_length], timezone.utc)
    time_stop = datetime.strptime(time[time_length-1],"%Y-%m-%dT%H:%M:%SZ")
    time_total = time_stop - time_start
    seconds = int(time_total.total_seconds())
    time_total_str = str(time_total)
    return time_total_str,seconds

def calculate_avg_spd(distance,time):
    v = (distance/time)*3600
    return v
