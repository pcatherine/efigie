#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from efigie import *
from efigie.forms import *
from efigie.views import *
from efigie.views.key import *

@login_required
@breadcrumbs(['index', 'keyNew'])
@csrf_protect
def keyNew(request):
  """
  New View

  Display a new form of :model:`efigie.Key`.

  **Templates**

    :template:`key/form.html`.

  **Context**

    form
      Form related to :model:`efigie.Key`.
    button
      New and Model's Name. Example: "New Key".
  """

  form = KeyForm(user=request.user, data=request.POST or None)

  if form.is_valid():
    form.save()
    messages.success(request, 'Chave <b>%s</b> criada com sucesso.' % (form.cleaned_data['name']))
    return redirect(keyList)

  return render(request, 'key/form.html',
    {'form': form,
     'button': 'Criar Chave'})
