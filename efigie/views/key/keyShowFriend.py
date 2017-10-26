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
@model_required(Key, 'keyList')
@breadcrumbs(['index', 'keyList', ('keyShow', 'keyId') ])
def keyShowFriend(request, keyId):
  """
  Display View

  Display an individual :model:`efigie.Key`.

  **Templates**

    :template:`key/show.html`.

  **Context**

    key
      A instance of :model:`efigie.Key`.
  """

  key = Key.objects.get(id = keyId)

  if request.user not in key.friends.all():
    redirect(keyList)

  return render(request, 'key/show_friend.html',
    {'key': key})
