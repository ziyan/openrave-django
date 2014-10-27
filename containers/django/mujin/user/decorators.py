from django.contrib.auth import authenticate
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from user.models import Key
from functools import wraps
import base64
import logging

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

def authenticated_view(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        request.user = None

        authorization = request.META.get('HTTP_AUTHORIZATION', '')
        if authorization and authorization.startswith('Basic '):
            parts = base64.b64decode(authorization.split(None, 1)[1]).split(':', 1)
            username = parts[0]
            password = ''
            if len(parts) == 2:
                password = parts[1]
            
            # try username password auth
            if username and password:
                user = authenticate(username=username, password=password)
                if user and user.is_active:
                    request.user = user

            # try with key auth
            if not request.user:
                try:
                    key = Key.objects.get(key=username or password)
                    if key and key.user and key.user.is_active:
                        request.user = key.user
                except Key.DoesNotExist:
                    pass

        if not request.user:
            response = HttpResponse(status=401)
            response['WWW-Authenticate'] = 'Basic realm=""'
            return response
        
        logging.warn('user: authenticated: id = %d, username = %s' % (request.user.id, request.user.username))  
        return func(request, *args, **kwargs)
    return wrapper
