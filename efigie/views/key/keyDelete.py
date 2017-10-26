#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from efigie.utils import invariants
from efigie.views.decorators import model_required

from efigie import *
from efigie.models import Key
from efigie.views import *
from efigie.views.key import *


@login_required
@model_required(Key, 'keyList', user = True)
@csrf_protect
def keyDelete(request, keyId):
  """
  Delete View.

  Deletes an individual :model:`efigie.Key`.
  """

  model_name = Key._meta.verbose_name
  key = Key.objects.get(id = keyId, user = request.user)
  name = key.name

  try:
    key.delete()
    messages.success(request, invariants.alert_delete_success % {
      'model_name': model_name, 
      'item_name': name})
  except Exception as e:
    messages.error(request, invariants.alert_delete_error % {
      'model_name': model_name, 
      'item_name': name})
  return redirect(keyList)
