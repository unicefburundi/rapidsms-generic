from django.conf.urls import patterns, include, url
from generic.views import *

urlpatterns = patterns('',
    url(r'^generic/(?P<content_id>\d+)/module/$', static_module),
)