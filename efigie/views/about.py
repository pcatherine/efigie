#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from efigie import *
from efigie.views import *

@login_required
def about(request, **kwargs):
  return render(request, 'about.html', 
    {'kwargs': kwargs,
     'breadcrumbs': ['index', 'about']})