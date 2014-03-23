from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.conf.urls import *
from trainstack_portal.views import createUser, groups, createGroup, topology, tasks, topologies
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html', }),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}),
    (r'', include('django.contrib.auth.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^$', groups),
    (r'^groups/$', groups),
    (r'^groups/create$', createGroup),
    (r'^users/create$', createUser),
    (r'^topologies/$', topologies),
    (r'^topologies/(\d+)$', topology),
    (r'^tasks/$', tasks),

)

    # Examples:
    # url(r'^$', 'trainstack_portal.views.home', name='home'),
    # url(r'^trainstack_portal/', include('trainstack_portal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
