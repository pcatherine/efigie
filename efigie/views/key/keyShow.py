#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render

from efigie.views.decorators import model_required, breadcrumbs

from efigie import *
from efigie.models import Key
from efigie.views import *
from efigie.views.key import *


@login_required
@model_required(Key, 'keyList', user = True)
@breadcrumbs(['index', 'keyList', ('keyShow', 'keyId') ])
def keyShow(request, keyId):
  """
  Display View

  Display an individual :model:`efigie.Key`.

  **Templates**

    :template:`key/show.html`.

  **Context**

    key
      A instance of :model:`efigie.Key`.
  """

  key = Key.objects.get(id = keyId, user = request.user)

  return render(request, 'key/show.html',
    {'key': key})
