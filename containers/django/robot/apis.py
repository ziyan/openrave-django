from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponse
from user.decorators import authenticated_view
from robot.decorators import robot_view
from robot.models import Robot
from functools import wraps

def api_view(methods=['GET']):
    def actual(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if request.method not in methods:
                return HttpResponseNotAllowed(methods)
            data = func(request, *args, **kwargs)
            if not data:
                return HttpResponse()
            if isinstance(data, HttpResponse):
                return data
            return JsonResponse(data)
        return wrapper
    return actual

@csrf_exempt
@authenticated_view
@api_view(['GET', 'POST'])
def robots(request):
    if request.method == 'GET':
        # list robot api
        return {'robots': [
            robot.to_dict() for robot in Robot.objects.all()
        ]}

    if request.method == 'POST':
        # create robot api
        robot = Robot(user=request.user, source=request.body, content_type=request.META['CONTENT_TYPE'])
        try:
            robot.save()
        except:
            return HttpResponseBadRequest()
        return {'robot': robot.to_dict()}

@csrf_exempt
@authenticated_view
@robot_view
@api_view(['GET', 'DELETE', 'PUT'])
def robot(request, robot, **kwargs):

    if request.method == 'GET':
        # get robot
        return {'robot': robot.to_dict(is_all=True)}

    if request.method == 'PUT':
        # modify robot
        robot.source = request.body
        robot.content_type = request.META['CONTENT_TYPE']
        try:
            robot.save()
        except:
            return HttpResponseBadRequest()
        return {'robot': robot.to_dict()}

    if request.method == 'DELETE':
        # delete robot
        Robot.objects.filter(id=robot.id).delete()
        return {'robot': robot.to_dict()}


urlpatterns = patterns('',
    url(r'^robots$', robots),
    url(r'^robots/(?P<id>[0-9]+)$', robot),
)



