# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from views import BookOnline

urlpatterns = patterns('',
    url(r'^book-online/$', BookOnline.as_view(), name='book_online'),
)
