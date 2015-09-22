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

from .models import Record
from .forms import RecordForm
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
        rev = reverse_lazy('booking:book_online')
        return '/booking/book-online/'
        assert False
        return reverse_lazy('booking:book_online')

    def form_invalid(self, form):
        result = super(BookOnline, self).form_invalid(form)
        print '--------------- form_invalid'
        print form.errors
        return result


class RecordsJson(View):
    def get(self, *args, **kwargs):
        print self.request.GET.get('doctor', '--------no doctors')
        self.doctor = get_object_or_404(Account, pk=self.request.GET.get('doctor', None))
        self.define_week_params()
        days = self.generate_day_objects()
        return JsonResponse(days, safe=False)

    def generate_day_objects(self):
        datetimes = self.get_busy_datetimes()
        print '----------------- get_busy_datetimes:'
        print datetimes
        now = datetime.now()
        days = []
        for num_day in range(0, 7):
            day_date = self.week_start + timedelta(days=num_day)
            hours = []
            # TODO брать часы приема из аккаунта и в зависимости от дня недели
            for h in range(9, 19):
                dt = datetime.combine(day_date, time(h, 0))
                print 'dt:{0} now:{1}  dt<now:{2}'.format(dt, now, dt<now)
                hours.append({
                    'label': '%d:00' % h,
                    'is_busy': True if dt in datetimes else False,
                    'in_past': True if dt < now else False,
                    'datetime_str': dt.strftime('%d.%m.%Y %H:%M:%S'),
                })
            day = {
                'date': day_date,
                'in_past': True if day_date < now.date() else False,
                'hours': hours
            }
            days.append(day)
        return days

    def get_busy_datetimes(self):
        print '----------- Record.objects.all().for_doctor(self.doctor):'
        print Record.objects.all().for_doctor(self.doctor)
        print '----------- Record.objects.all().for_doctor(self.doctor).filter( datetime__lte=self.week_start, datetime__gte=self.week_end,):'
        print self.week_start
        print self.week_end
        print Record.objects.all().for_doctor(self.doctor).filter( datetime__gte=datetime.combine(self.week_start, time(0, 0, 1)), datetime__lte=datetime.combine(self.week_end, time(23, 59, 59)),)
        datetimes = Record.objects.all().for_doctor(self.doctor).filter(
            datetime__gte=datetime.combine(self.week_start, time(0, 0, 1)),
            datetime__lte=datetime.combine(self.week_end, time(23, 59, 59)),
        ).values_list('datetime', flat=True)
        return datetimes

    def define_week_params(self):
        date_from = self.request.GET.get('date_from', None)

        if not date_from:
            date_from = date.today()
        else:
            date_from = datetime.strptime(date_from, '%d.%m.%Y').date()

        print date_from
        last_monday = date_from + relativedelta(weekday=MO(-1))
        date_from = last_monday

        # week_range = [date_from]
        # for num_day in range(2, 8):
        #     d = date_from + timedelta(days=num_day)
        #     week_range.append(d)
        self.week_start = date_from
        self.week_end = date_from + timedelta(days=7)
