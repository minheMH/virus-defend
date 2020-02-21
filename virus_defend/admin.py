from django.contrib import admin
from .models import Healthstate
class HealthstateAdmin(admin.ModelAdmin ):
    list_display = ('temp','state','place','pub_time')
    list_filter = ('place',)
admin.site.register(Healthstate,HealthstateAdmin)