# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

from app.account.models import Account


class RecordQueryset(models.query.QuerySet):
    def for_doctor(self, doctor):
        """
        Отбирает записи лишь к указанному доктору.
        """
        return self.filter(doctor=doctor)

    def by_period(self, date_from, date_to):
        """
        Отбирает записи за указанный период.
        """
        return self.filter(
            datetime__gte=date_from,
            datetime__lte=date_to,
        )


class RecordManager(models.Manager):
    def get_queryset(self):
        return RecordQueryset(self.model).all()

    def get_busy_datetimes(self, doctor, date_from, date_to):
        """
        Возвращает список дат (со временем), в которые у указанного доктора
        уже имеется запись на прием.
        """
        datetimes = Record.objects.all().for_doctor(doctor).by_period(date_from, date_to).values_list('datetime', flat=True)
        return datetimes


class Record(models.Model):
    datetime = models.DateTimeField(verbose_name=_(u'Дата и время приема'))
    patient_fio = models.CharField(max_length=60, verbose_name=_(u'ФИО пациента'))
    doctor = models.ForeignKey('account.Account', limit_choices_to={'is_active': True, 'employee_type': Account.EMPLOYEE_TYPE_DOCTOR}, verbose_name=_(u'Врач'))

    objects = RecordManager()

    class Meta:
        verbose_name = _(u'Запись на прием к врачу')
        verbose_name_plural = _(u'Записи на прием к врачу')

