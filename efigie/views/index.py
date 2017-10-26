#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from efigie.views.decorators import breadcrumbs
from efigie.views import *


@login_required
@breadcrumbs(['index'])
def index(request):

  return render(request, 'index.html')
