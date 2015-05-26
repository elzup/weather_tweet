from django.contrib import admin
from cms.models import RainMeshMap

admin.site.register(RainMeshMap)

class RainMeshMapAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_map',)
