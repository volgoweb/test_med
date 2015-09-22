# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _

from app.account.models import Account


class RecordQueryset(models.query.QuerySet):
    def for_doctor(self, doctor):
        return self.filter(doctor=doctor)


class RecordManager(models.Manager):
    def get_queryset(self):
        return RecordQueryset(self.model).all()


class Record(models.Model):
    datetime = models.DateTimeField(verbose_name=_(u'Дата и время приема'))
    patient_fio = models.CharField(max_length=60, verbose_name=_(u'ФИО пациента'))
    doctor = models.ForeignKey('account.Account', limit_choices_to={'is_active': True, 'employee_type': Account.EMPLOYEE_TYPE_DOCTOR}, verbose_name=_(u'Врач'))

    objects = RecordManager()

    class Meta:
        verbose_name = _(u'Запись на прием к врачу')
        verbose_name_plural = _(u'Записи на прием к врачу')

