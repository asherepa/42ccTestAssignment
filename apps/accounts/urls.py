from django.conf.urls import patterns, url

from apps.accounts.views import index

urlpatterns = patterns('apps.accounts.views',
    url(r'^$', index.as_view(), name='index'),
)
