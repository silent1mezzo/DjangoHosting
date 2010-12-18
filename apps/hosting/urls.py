from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'hosting.views.index', name='index'),
    url(r'^(?P<host_slug>\w+)/$', 'hosting.views.view_host', name='view_host'),
	url(r'^about/$', 'hosting.views.about', name='about'),
	url(r'^contact/$', 'hosting.views.contact', name='contact'),
)
