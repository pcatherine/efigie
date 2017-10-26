#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from efigie.utils import invariants
from efigie.views.decorators import model_required, breadcrumbs

from efigie.forms import *
from efigie.models import Key
from efigie.views import *
from efigie.views.key import *

@login_required
@model_required(Key, 'keyList', user = True)
@breadcrumbs(['index', 'keyList', ('keyShow', 'keyId'), ('keyEdit','keyId')])
@csrf_protect
def keyEdit(request, keyId):
  """
  Edit View

  Display an edit form of :model:`efigie.Key`.

  **Templates**

    :template:`key/form.html`.

  **Context**

    title
      Key's name
    form
      Form related to :model:`efigie.Key`.
    button
      Update and Model's Name. Example: "Update Key".
  """

  model_name = Key._meta.verbose_name
  key = Key.objects.get(id = keyId, user = request.user)
  form = KeyForm(user=request.user, instance=key, data=request.POST or None)

  if form.is_valid():
    form.save()
    messages.success(request, invariants.alert_update_success % {
      'model_name': model_name, 
      'item_name': key.name})
    return redirect(keyShow, keyId=keyId)

  return render(request, 'key/form.html',
    {'title': ': <b>%s</b>' % (key.name),
     'form': form,
     'button': invariants.button_edit })
