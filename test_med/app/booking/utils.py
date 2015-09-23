# -*- coding: utf-8 -*-
from django.conf import settings

def get_working_weekday_nums():
    """
    Возвращает номера рабочих дней недели, начиная с нуля.
    """
    weekday_nums = range(0, 7)
    return set(weekday_nums) - set(settings.APP_WEEKENDS)

