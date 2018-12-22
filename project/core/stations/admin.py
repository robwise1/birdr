from django.contrib import admin

from stations.models import Station

class StationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Station, StationAdmin)