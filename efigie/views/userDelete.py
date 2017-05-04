#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from efigie import *
from efigie.views import *
#AGARD
@login_required
def userDelete(request):
  return redirect(userSettings)