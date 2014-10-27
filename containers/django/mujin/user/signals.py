from django.dispatch import receiver
from django.db.models.signals import pre_save
from user import security
from user.models import Key

@receiver(pre_save, sender=Key, dispatch_uid='key_pre_save')
def key_pre_save(sender, instance, **kwargs):
    instance.key = instance.key or security.generate_random_string(length=64)
