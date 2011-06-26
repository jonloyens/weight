from django.conf.urls.defaults import patterns, include, url

from demo.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', DemoView.as_view(), {'template':'findinterests'}, name='home', ),
    url(r'^(?P<template>\w+)/$', DemoView.as_view(), name='templates'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

)
