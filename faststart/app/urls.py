from django.conf.urls.defaults import *

urlpatterns = patterns('faststart.app.views',
       url(r'^$', 'view1', name='view1'),
       )
