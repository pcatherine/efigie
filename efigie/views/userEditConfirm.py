#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from efigie import *
from efigie.views import *

@login_required
def userEditConfirm(request, key, **kwargs):
  return userNewConfirm(request, key)