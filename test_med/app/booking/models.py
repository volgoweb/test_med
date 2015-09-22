# -*- coding: utf-8 -*-
from django.db import models


class RecordQueryset(models.query.QuerySet):
    def for_doctor(self, doctor):
        return self.filter(doctor=doctor)


class RecordManager(models.Manager):
    def get_queryset(self):
        return RecordQueryset(self.model).all()


class Record(models.Model):
    datetime = models.DateTimeField(verbose_name=u'Дата и время приема')
    patient_fio = models.CharField(max_length=60, verbose_name=u'ФИО пациента')
    doctor = models.ForeignKey('account.Account', verbose_name=u'Врач')

    objects = RecordManager()


