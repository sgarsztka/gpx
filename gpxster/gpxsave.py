import time
import os
from django.conf import settings

def handle_uploaded_file(f):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    base_dir =settings.MEDIA_ROOT
    filename = os.path.join(base_dir, str(timestr)+str('.gpx'))

    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
