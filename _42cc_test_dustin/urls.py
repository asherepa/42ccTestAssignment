from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('apps.accounts.urls', namespace="accounts")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^requests/', include('apps.rlogger.urls', namespace="requests")),
    url(r'^accounts/login/$', login,
        {'template_name': 'accounts/login_base.html',
         'extra_context': {'next': '/accounts/edit/'}}),
    url(r'^accounts/logout/$', logout, {'next_page': '/'}),
)


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
