#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.shortcuts import render

from efigie import *
from efigie.views import *

def bad_request(request):
  return render(request, '400.html', status=400)

def permission_denied(request):
  return render(request, '403.html', status=403)

def page_not_found(request, exceptions):
  return render(request, '404.html',{'exceptions': exceptions}, status=404)

def server_error(request):
  return render(request, '500.html', status=500)