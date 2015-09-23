# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _

from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
        widgets = {
            'datetime': forms.HiddenInput,
        }

    def __init__(self, *args, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].widget.attrs['ng-model'] = 'record.doctor'
        self.fields['doctor'].widget.attrs['ng-change'] = 'dt.updateWeek()'
        self.fields['datetime'].widget.attrs['ng-model'] = 'record.datetime'
        self.fields['datetime'].input_formats = ['%d.%m.%Y %H:%M:%S']
        # self.fields['datetime'].widget.attrs['ng-change'] = 'change()'

    def clean(self):
        self.cleaned_data = super(RecordForm, self).clean()
        doctor = self.cleaned_data.get('doctor')
        datetime = self.cleaned_data.get('datetime')
        if Record.objects.filter(doctor=doctor, datetime=datetime).exists():
            raise forms.ValidationError(_(u'Извините произошла ошибка. Выбранное вами время у врача %(name)s занято.' % {'name': doctor}))
        return self.cleaned_data
