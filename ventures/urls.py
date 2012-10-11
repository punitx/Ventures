from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^applications/', include(
                           'ventures.applications.urls')),
                       url(r'^resources/', include(
                           'ventures.resources.urls')),
                       url(r'^volunteers/', include(
                           'ventures.volunteers.urls')),
                       url(r'^judges/', include(
                           'ventures.judges.urls')),
                       )

if settings.DEBUG:
# static files (images, css, javascript, etc.)
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
         'document_root': settings.MEDIA_ROOT}))
