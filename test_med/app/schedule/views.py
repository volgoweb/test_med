# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
# from django.views.generic import ListView
from django.views.generic import CreateView


class BookOnline(CreateView):
    template_name = 'schedule/book_page.html'
