from django.conf.urls import patterns, url
from .views import index


urlpatterns = patterns('apps.rlogger.views',
    url(r'^$', index.as_view(), name='index'),
)
