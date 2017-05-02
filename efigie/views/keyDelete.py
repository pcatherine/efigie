#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from efigie import *
from efigie.models import Key
from efigie.views import *

@login_required
def keyDelete(request, keyId):
  keyName = None
  try:
    key = Key.objects.get(id = keyId)
    keyName = key
    key.delete()
    messages.success(request, 'Chave <b>%s</b> deletada com sucesso.' % (keyName.identifier))
  except Exception as e:
    messages.error(request, 'Chave <b>%s</b> não pode ser deletada.' % (keyName.identifier))

  return redirect(keyList)