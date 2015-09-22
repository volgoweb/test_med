# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='time_zone',
        ),
        migrations.AlterField(
            model_name='account',
            name='job',
            field=models.CharField(max_length=50, null=True, verbose_name='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c', blank=True),
        ),
    ]
