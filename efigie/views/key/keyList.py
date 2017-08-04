#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.forms.models import fields_for_model
from django.shortcuts import render

from efigie.views.decorators import breadcrumbs

from efigie import *
from efigie.models import Key
from efigie.views import *
from efigie.views.key import *


@login_required
@breadcrumbs(['index', 'keyList'])
def keyList(request):
  """
  List View

  Display all :model:`efigie.Key` that the user has permission.

  **Templates**

    :template:`key/list.html`.

  **Context**

    tableHead
      Table head with label of: "name" and "size".
    regions
      List of :model:`efigie.Key`.
  """

  keys = Key.objects.filter(user = request.user).order_by('name')

  return render(request, 'key/list.html',
    {'tableHead': fields_for_model(Key, fields=('name', 'size')),
     'keys': keys})
