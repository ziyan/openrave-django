from django.conf.urls import patterns, url
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from user.decorators import user_view

def users(request):
    return JsonResponse({
        'users': [],
    })

@user_view
def user(request, user, **kwargs):
    robots = user.robots.all()

    return JsonResponse({
        'user': {
            'id': user.username,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'robots': [robot.id for robot in robots],
        },
        'robots': [
            robot.to_dict()
            for robot in robots
        ]
    })

urlpatterns = patterns('',
    url(r'^users$', users),
    url(r'^users/(?P<id>[0-9]+)', user),
)

