# -*- coding: utf-8 -*-
from django.contrib import admin

from app.account.models import Account
from .models import Record

class DoctorFilter(admin.SimpleListFilter):
    title = u'Врач'
    parameter_name = 'doctor'

    def lookups(self, request, model_admin):
        return tuple([(row.pk, row) for row in Account.objects.get_doctors_for_book()])

    def queryset(self, request, queryset):
        val = self.value()
        if val:
            return queryset.filter(doctor__pk=val)
        return queryset

class RecordAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'doctor', 'patient_fio')
    list_filter = (DoctorFilter, 'patient_fio',)
    ordering = ('datetime',)

admin.site.register(Record, RecordAdmin)
