#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from efigie import *
from efigie.models import Key
from efigie.views import *

@login_required
def keyShow(request, keyId):
  breadcrumbs = ['index', 'keyList', 'keyShow']

  try:
    key = Key.objects.get(id = keyId)
    messages.error(request, '<p>Excluiremos a chave: <b>%s</b> permanentemente.</p>' % (key.name) , extra_tags='model')
    return render(request, 'key_show.html',
      {'key': key,
      'breadcrumbs': breadcrumbs})

  except Exception as e:
    print(e)
    messages.error(request, 'Chave não pode ser exibida.')
    return redirect(keyList)

  