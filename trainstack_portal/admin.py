from django.contrib import admin
from trainstack_portal.models import topology

class topologyAdmin(admin.ModelAdmin):
    pass
admin.site.register(topology, topologyAdmin)
