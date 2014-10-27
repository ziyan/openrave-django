from django.http import Http404
from robot.models import Robot
from functools import wraps

def robot_view(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            robot = Robot.objects.get(id=kwargs['id'])
        except Robot.DoesNotExist:
            raise Http404

        kwargs['robot'] = robot
        return func(request, *args, **kwargs)
    return wrapper

