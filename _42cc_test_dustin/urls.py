from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('apps.accounts.urls')),
    url(r'request/', include('apps.rlogger.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
