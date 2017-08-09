#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from efigie.views import *
from efigie.forms import *

@csrf_protect
@login_required
def keyEdit(request, keyId):
  breadcrumbs = ['index', 'keyList', 'keyEdit']

  try:
    key = Key.objects.get(id = keyId)
    form = KeyEditForm(user=request.user, key=key, data=request.POST or None)
    
    if form.is_valid():
      form.save()
      messages.success(request, 'Chave <b>%s</b> editada com sucesso.' % (form.cleaned_data['name']))
      return redirect(keyShow, keyId=keyId)
  except Exception as e:
    messages.error(request, 'Chave <b>%s</b> não pode ser editada.' % (form.cleaned_data['name']))
    return redirect(keyList)

  return render(request, 'form.html',
    {'title': ': <b>%s</b>' % (key.name),
     'form': form,
     'button': 'Editar',
     'breadcrumbs': breadcrumbs})