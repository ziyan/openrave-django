# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(verbose_name='key', unique=True, max_length=64, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('user', models.ForeignKey(related_name='keys', verbose_name='user', to=settings.AUTH_USER_MODEL, help_text='Owner of the key.')),
            ],
            options={
                'verbose_name': 'key',
                'verbose_name_plural': 'keys',
            },
            bases=(models.Model,),
        ),
    ]
