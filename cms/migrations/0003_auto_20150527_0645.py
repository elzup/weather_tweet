# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20150527_0343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rainmesh',
            old_name='map_id',
            new_name='map',
        ),
        migrations.RenameField(
            model_name='rainmesh',
            old_name='mesh_position_id',
            new_name='mesh_position',
        ),
    ]
