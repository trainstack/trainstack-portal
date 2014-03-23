from django.contrib import admin
from trainstack_portal.models import Topology

class TopologyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Topology, TopologyAdmin)
