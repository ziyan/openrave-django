from django.contrib import admin
from robot.models import Robot

class RobotAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'name', 'description', 'user', 'created', 'modified']

admin.site.register(Robot, RobotAdmin)
