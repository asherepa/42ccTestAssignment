from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('apps.accounts.urls')),
    url(r'^accounts/', include('apps.accounts.urls')),
    url(r'^request/', include('apps.rlogger.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
