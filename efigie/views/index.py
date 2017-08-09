#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.views.decorators.csrf import csrf_protect

from efigie.views.decorators import breadcrumbs
from efigie.views import *

import efigie.config as config


# @login_required
@breadcrumbs(['index'])
def index(request):
  from django.core.signing import Signer
  signer = Signer()
  value = signer.sign('PAOLLA')
  original = signer.unsign(value)
  print(value)
  print(original)

  return render(request, 'about.html')
