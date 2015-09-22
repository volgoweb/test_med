# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from views import BookOnline, RecordsJson

urlpatterns = patterns('',
    url(r'^book-online/$', BookOnline.as_view(), name='book_online'),
    url(r'^get-days-for-booking/$', RecordsJson.as_view(), name='get_days_for_booking'),
)
