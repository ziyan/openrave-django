from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from yamlfield.fields import YAMLField

class Robot(models.Model):

    # basic
    name = models.CharField(
        max_length=64,
        verbose_name=_('name'),
        help_text=_('Name of the robot.'),
    )

    description = models.TextField(blank=True, verbose_name=_('description'))

    # owner
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name='robots',
        on_delete=models.SET_NULL,
        verbose_name=_('user'),
        help_text=_('Owner of the robot.'),
    )

    data = YAMLField(blank=True, verbose_name=_('data'))
    source = models.BinaryField(verbose_name=_('source'))

    # meta
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    modified = models.DateTimeField(auto_now=True, verbose_name=_('modified'))

    class Meta:
        verbose_name = _('robot')
        verbose_name_plural = _('robots')

    def __unicode__(self):
        return self.name

