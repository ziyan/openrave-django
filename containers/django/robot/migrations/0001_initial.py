# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import yamlfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name of the robot.', max_length=64, verbose_name='name', blank=True)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('data', yamlfield.fields.YAMLField(verbose_name='data', blank=True)),
                ('source', models.BinaryField(verbose_name='source')),
                ('content_type', models.CharField(default=b'application/xml', max_length=64, verbose_name='content type', choices=[(b'application/xml', b'application/xml'), (b'application/zip', b'application/zip')])),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('user', models.ForeignKey(related_name='robots', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, help_text='Owner of the robot.', null=True, verbose_name='user')),
            ],
            options={
                'verbose_name': 'robot',
                'verbose_name_plural': 'robots',
            },
            bases=(models.Model,),
        ),
    ]
