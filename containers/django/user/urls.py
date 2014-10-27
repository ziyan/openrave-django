from django.conf.urls import patterns, url

urlpatterns = patterns('user.views',
    url(r'^user/(?P<id>[0-9]+)$', 'user', name='user'),
)
