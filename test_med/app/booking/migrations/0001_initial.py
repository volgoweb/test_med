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
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043f\u0440\u0438\u0435\u043c\u0430')),
                ('patient_fio', models.CharField(max_length=60, verbose_name='\u0424\u0418\u041e \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430')),
                ('doctor', models.ForeignKey(verbose_name='\u0412\u0440\u0430\u0447', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
