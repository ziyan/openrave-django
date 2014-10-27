from django.dispatch import receiver
from django.db.models.signals import pre_save
from robot import utils
from robot.models import Robot

@receiver(pre_save, sender=Robot, dispatch_uid='robot_pre_save')
def robot_pre_save(sender, instance, **kwargs):
    instance.data = utils.load(instance.source, instance.content_type)
    instance.name = instance.name or instance.data.get('name', '')
    instance.description = instance.description or instance.data.get('description', '')
