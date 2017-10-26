#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from efigie.forms import *
from efigie.models import UserEffigy
from efigie.views import *
from efigie.views.message import *
from efigie.utils import invariants

@login_required
def messageSettings(request):
  form = MessageSettingsForm(request.POST or None, request.FILES or None, user=request.user)

  settingsName = UserEffigy._meta.get_field('settings').verbose_name

  if form.is_valid():
    form.save()
    messages.success(request, invariants.alert_update_success % {
    	'model_name': "", 
    	'item_name': settingsName})

  return render(request, 'message/form.html',
    {'form': form,
     'button': invariants.button_edit })
