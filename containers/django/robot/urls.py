from django.conf.urls import patterns, url

urlpatterns = patterns('robot.views',
    url(r'^robot/(?P<id>[0-9]+)$', 'robot', name='robot'),
)

