from django.db import models
from geoposition.fields import GeopositionField

class MeshPosition(models.Model):
    """メッシュ緯度経度"""
    position = GeopositionField()

class RainMeshMap(models.Model):
    """メッシュ地図"""
    time_map = models.DateTimeField(auto_now_add=False)

class RainMesh(models.Model):
    """メッシュ"""
    rain_rate_x10 = models.SmallIntegerField()
    map_id = models.ForeignKey(RainMeshMap, verbose_name='メッシュ緯度経度', related_name='meshes')
    mesh_position_id = models.ForeignKey(MeshPosition, verbose_name='メッシュ地図', related_name='meshes')
