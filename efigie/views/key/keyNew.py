#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from efigie.utils import invariants
from efigie.views.decorators import model_required, breadcrumbs

from efigie import *
from efigie.forms import *
from efigie.models import Key
from efigie.views import *
from efigie.views.key import *

@login_required
@breadcrumbs(['index', 'keyList', 'keyNew'])
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
    key = form.save()
    messages.success(request, invariants.alert_add_success % {
      'model_name': Key._meta.verbose_name, 
      'item_name': key.name } )
    return redirect(keyList)

  return render(request, 'key/form.html',
    {'form': form,
     'button': invariants.button_new })
