# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='email address')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('middle_name', models.CharField(max_length=30, null=True, verbose_name='middle name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u0410\u043a\u0442\u0438\u0432\u0435\u043d')),
                ('job', models.CharField(max_length=50, null=True, verbose_name='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c', blank=True)),
                ('employee_type', models.CharField(max_length=20, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u0430', choices=[(b'doctor', '\u0414\u043e\u043a\u0442\u043e\u0440'), (b'manager', '\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440')])),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
                ('can_book', models.BooleanField(default=False, verbose_name='\u041e\u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043b\u044f\u0435\u0442 \u043f\u0440\u0438\u0435\u043c \u043f\u043e \u0437\u0430\u043f\u0438\u0441\u0438')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a',
                'verbose_name_plural': '\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438',
            },
        ),
    ]
