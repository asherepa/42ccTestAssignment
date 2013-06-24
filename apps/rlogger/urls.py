from django.conf.urls import patterns, url
from .views import index, event


urlpatterns = patterns(
    'apps.rlogger.views',
    url(r'^$', index, name='index'),
    url(r'^(?P<event_id>\d+)/$', event, name='event'),
)
