# -*- coding:utf-8 -*-
from datetime import date, timedelta, datetime, time
from dateutil.relativedelta import relativedelta, MO

# from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, JsonResponse
from django.views.generic import CreateView, View
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

from .models import Record
from .forms import RecordForm
from .utils import get_working_weekday_nums
from app.account.models import Account

class BookOnline(CreateView):
    model = Record
    template_name = 'booking/book_page.html'
    form_class = RecordForm

    def get_context_data(self, *args, **kwargs):
        context = super(BookOnline, self).get_context_data(*args, **kwargs)
        hour_labels = []
        # TODO брать часы приема из аккаунта и в зависимости от дня недели
        for h in range(9, 19):
            hour_labels.append('%d:00' % h)
        context.update({
            'hour_labels': hour_labels,
        })
        return context

    def form_valid(self, form):
        result = super(BookOnline, self).form_valid(form)
        rec = form.save()
        messages.success(self.request, u'Вы записаны к врачу {0} на {1}'.format(rec.doctor, rec.datetime.strftime('%d.%m.%Y %H:%M')))
        return result

    def get_success_url(self):
        return reverse_lazy('booking:book_online')


class RecordsWeekJson(View):
    def get(self, *args, **kwargs):
        self.doctor = get_object_or_404(Account, pk=self.request.GET.get('doctor', None))
        self.define_period_params()
        days = self.generate_day_objects()
        return JsonResponse(days, safe=False)

    def generate_day_objects(self):
        datetimes = Record.objects.get_busy_datetimes(
                doctor=self.doctor,
                date_from=datetime.combine(self.period_start, time(0, 0, 1)),
                date_to=datetime.combine(self.period_end, time(23, 59, 59)),
        )
        now = datetime.now()
        days = []
        for num_day in get_working_weekday_nums():
            day_date = self.period_start + timedelta(days=num_day)
            hours = []
            # TODO брать часы приема из аккаунта и в зависимости от дня недели
            for h in range(settings.APP_DAY_START.hour, settings.APP_DAY_END.hour + 1):
                dt = datetime.combine(day_date, time(h, 0))
                hours.append({
                    'label': '%d:00' % h,
                    'is_busy': True if dt in datetimes else False,
                    'in_past': True if dt < now else False,
                    'datetime_str': dt.strftime('%d.%m.%Y %H:%M:%S'),
                })
            from django.utils import formats
            day = {
                'label': formats.date_format(datetime.combine(day_date, time(0,0,1)), 'WEEK_DAY_DATE_FORMAT'),
                'in_past': True if day_date < now.date() else False,
                'hours': hours
            }
            days.append(day)
        return days

    def define_period_params(self):
        """
        Исходя из GET-параметров определяем период, по которому нужно возвратить данные.
        """
        date_from = self.request.GET.get('date_from', None)

        if not date_from:
            date_from = date.today()
        else:
            date_from = datetime.strptime(date_from, '%d.%m.%Y').date()

        last_monday = date_from + relativedelta(weekday=MO(-1))
        date_from = last_monday

        self.period_start = date_from
        self.period_end = date_from + timedelta(days=7)
