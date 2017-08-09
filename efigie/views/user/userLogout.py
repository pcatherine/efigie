#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

from efigie import *
from efigie.views import *
from efigie.views.user import *


@login_required
def userLogout(request):
  logout(request)
  return redirect(userLogin)
