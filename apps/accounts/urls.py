from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

from apps.accounts.views import index, edit


urlpatterns = patterns('apps.accounts.views',
    url(r'^$', index),
    url(r'^login/$', login, {'template_name': 'accounts/base_login.html'}),
    url(r'^logout/$', logout),
    url(r'^edit/', edit, name='edit'),
)
