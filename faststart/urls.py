from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template


admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('faststart.app.urls')),

    #admin
    (r'^admin/(.*)$', admin.site.root),
    )

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'), 'serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )