#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from efigie.views.decorators import breadcrumbs
from efigie.views import *

@login_required
@breadcrumbs(['index', 'systemSettings'])
@csrf_protect
def systemSettings(request):

  return render(request, "settings.html")
