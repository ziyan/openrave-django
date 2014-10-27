from django.shortcuts import render
from django.http import HttpResponse
from user.decorators import authenticated_view
from robot.decorators import robot_view

@authenticated_view
@robot_view
def robot(request, robot, **kwargs):
    return render(request, 'app.html')

