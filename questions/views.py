# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView

from pprint import pformat
from urlparse import parse_qsl


class AboutView(TemplateView):
    template_name = "about.html"


def get_post(request):
    data = []
    if request.method == 'GET':
        data = request.GET
    elif request.method == 'POST':
        data = request.POST

    return render(request, 'about.html', {'method' : request.method,
                                          'data' : data})