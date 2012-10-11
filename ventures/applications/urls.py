from django.conf.urls.defaults import *

urlpatterns = patterns('ventures.applications.views',
                       (r'^$', 'index'),
                       )
