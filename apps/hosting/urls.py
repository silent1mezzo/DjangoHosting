from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'hosting.views.index', name='index'),
)
