from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from functools import wraps

def user_view(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            user = User.objects.get(id=kwargs['id'])
        except User.DoesNotExist:
            raise Http404

        kwargs['user'] = user
        return func(request, *args, **kwargs)
    return wrapper

