from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include('user.apis')),
    url(r'^api/', include('robot.apis')),

    url(r'', include('web.urls', namespace='web')),
    url(r'', include('user.urls', namespace='user')),
    url(r'', include('robot.urls', namespace='robot')),
)

