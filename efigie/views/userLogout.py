#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

from efigie import *
from efigie.views import *

@login_required
def userLogout(request, **kwargs):
  logout(request)
  return redirect(userLogin)
