from django.conf.urls import patterns, url
from .views import index, edit


urlpatterns = patterns(
    'apps.accounts.views',
    url(r'^$', index.as_view(), name='index'),
    url(r'^accounts/edit/$', edit, name='edit'),
)
