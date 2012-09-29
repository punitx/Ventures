from django.conf.urls.defaults import *

urlpatterns = patterns('ventures.volunteers.views',
                       (r'^$', 'index'),
                       )
