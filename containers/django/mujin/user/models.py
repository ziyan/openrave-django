from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from user import security

class Key(models.Model):

    key = models.CharField(
        max_length=64,
        editable=False,
        unique=True,
        verbose_name=_('key'),
    )

    user = models.ForeignKey(
        User,
        related_name='keys',
        verbose_name=_('user'),
        help_text=_('Owner of the key.'),
    )

    # meta
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    modified = models.DateTimeField(auto_now=True, verbose_name=_('modified'))

    class Meta:
        verbose_name = _('key')
        verbose_name_plural = _('keys')

    def __unicode__(self):
        return self.key

