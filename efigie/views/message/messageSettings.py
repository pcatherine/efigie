#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from efigie.forms import *
from efigie.views import *

@login_required
def messageSettings(request):
  form = MessageSettingsForm(request.POST or None, request.FILES or None, user=request.user)
  if form.is_valid():
    form.save()


  return render(request, 'message/form.html',
    {'form': form,
     'button': 'Save'})
