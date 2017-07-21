#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from efigie import *
from efigie.models import Key
from efigie.views import *

@login_required
def keyList(request):
  breadcrumbs = ['index', 'keyList']

  keyList = Key.objects.filter(user = request.user).order_by('name')
  
  return render(request, 'key_list.html',
    {'keyList': keyList,
    'breadcrumbs':breadcrumbs})