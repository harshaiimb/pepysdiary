# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('allow_registration', models.BooleanField(default=True)),
                ('allow_login', models.BooleanField(default=True)),
                ('allow_comments', models.BooleanField(default=True)),
                ('use_registration_captcha', models.BooleanField(default=False, help_text=b'If checked, people must complete a Captcha field when registering.')),
                ('use_registration_question', models.BooleanField(default=False, help_text=b'If checked, people must successfully answer the question below when registering.')),
                ('registration_question', models.CharField(default=b'', max_length=255, blank=True)),
                ('registration_answer', models.CharField(default=b'', help_text=b'Not case-sensitive.', max_length=255, blank=True)),
                ('site', models.OneToOneField(to='sites.Site')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
