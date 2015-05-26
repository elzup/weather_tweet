# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeshPosition',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
            ],
        ),
        migrations.CreateModel(
            name='RainMesh',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('rain_rate_x10', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RainMeshMap',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('time_map', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='rainmesh',
            name='map_id',
            field=models.ForeignKey(verbose_name='メッシュ緯度経度', to='cms.RainMeshMap', related_name='meshes'),
        ),
        migrations.AddField(
            model_name='rainmesh',
            name='mesh_position_id',
            field=models.ForeignKey(verbose_name='メッシュ地図', to='cms.MeshPosition', related_name='meshes'),
        ),
    ]
