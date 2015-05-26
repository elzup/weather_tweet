from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from geoposition import Geoposition
from cms.models import RainMeshMap, RainMesh, MeshPosition
import csv

def import_data(request):
    """降水量データcsv のインポートみ込み"""
    day = 20
    hour = 23
    minute = 21
    file_name = "./data/test_2015-05-%02d_%02d-%02d.csv" % (day, hour, minute)

    with open(file_name) as f:
        reader = csv.reader(f)
        header = next(reader)

        time_map = timezone.datetime(2015, 5, day, hour, minute)
        try:
            rain_map = RainMeshMap.objects.get(time_map=time_map)
        except ObjectDoesNotExist:
            rain_map = RainMeshMap(time_map=time_map)
            rain_map.save()

        print(rain_map)
        print(rain_map.id)

        c = 0
        for row in reader:
            lat, lng, rate = map(float, row)
            if rate == 0:
                continue
            try:
                pos = MeshPosition.objects.get(position=Geoposition(lat, lng))
                print('skip')
            except ObjectDoesNotExist:
                pos = MeshPosition(position=Geoposition(lat, lng))
                pos.save()
            try:
                mesh = RainMesh.objects.get(map_id=rain_map.id, mesh_position_id=pos.id)
                print('skip')
            except ObjectDoesNotExist:
                mesh = RainMesh(map_id=rain_map.id, mesh_position_id=pos.id, rain_rate_x10=int(rate * 10))
                mesh.save()

            c += 1
            print(lat, lng, rate)
            print(mesh.id)
            print(c)
            if c == 20:
                break

    return HttpResponse(u'インポート')
