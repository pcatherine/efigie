#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from efigie import *
from efigie.views import *

@login_required
def index(request, **kwargs):
<<<<<<< HEAD

  return render(request, 'index.html',
    {'kwargs': kwargs})
=======
  return render(request, 'index.html')
>>>>>>> master
