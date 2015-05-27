from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.utils import timezone
from geoposition import Geoposition
from cms.models import RainMeshMap, RainMesh, MeshPosition
import csv


def regist_mesh(rain_map, lat, lng, rate):
    # 明らかにおかしなデータが混じっていたので
#    if lat < 35.0 or lat >= 38 or lng < 137.0 or lng >= 139:
#        return
    # データ数が多いため地域を制限
    if lat < 35.61 or lat >= 35.80 or lng < 139.46 or lng >= 139.85:
        return
    if rate == 0:
        return
    try:
        pos = MeshPosition.objects.get(position=Geoposition(lat, lng))
    except ObjectDoesNotExist:
        pos = MeshPosition(position=Geoposition(lat, lng))
        pos.save()
    try:
        mesh = RainMesh.objects.get(map_id=rain_map.id, mesh_position_id=pos.id)
    except ObjectDoesNotExist:
        mesh = RainMesh(map_id=rain_map.id, mesh_position_id=pos.id, rain_rate_x10=int(rate * 10))
        mesh.save()

def import_data(request):
    """降水量データcsv のインポートみ込み"""
    # 開始日
#    itime = timezone.datetime(2015, 5, 20, 23, 23)
    itime = timezone.datetime(2015, 5, 20, 23, 35)
    end_time = timezone.datetime(2015, 5, 21, 6, 40)

    min1 = timezone.timedelta(minutes=10)

    while(itime <= end_time):
        file_name = "./data/test_2015-05-%02d_%02d-%02d.csv" % (itime.date().day, itime.hour, itime.minute)
        print(file_name)
        try:
            with open(file_name) as f:
                reader = csv.reader(f)
                header = next(reader)
                time_map = itime
                try:
                    rain_map = RainMeshMap.objects.get(time_map=time_map)
                except ObjectDoesNotExist:
                    rain_map = RainMeshMap(time_map=time_map)
                    rain_map.save()
                for row in reader:
                    lat, lng, rate = map(float, row)
                    regist_mesh(rain_map, lat, lng, rate)
        except FileNotFoundError:
            print('no file')
        itime += min1

    return HttpResponse(u'インポート')
