# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Record

class RecordAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'doctor', 'patient_fio')
    list_filter = ('doctor',)
    ordering = ('datetime',)


admin.site.register(Record, RecordAdmin)
