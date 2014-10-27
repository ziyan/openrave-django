from django.shortcuts import render
from django.http import HttpResponse
from robot.decorators import robot_view

@robot_view
def robot(request, robot, **kwargs):
    return render(request, 'app.html')

