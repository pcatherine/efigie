#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.shortcuts import render, redirect

from efigie.views.decorators import model_required, breadcrumbs

from efigie import *
from efigie.models import Friend, Notification
from efigie.views import *
from efigie.views.friend import *


@login_required
@breadcrumbs(['index', 'friendList', 'friendBlockedList'])
def friendBlockedList(request):
  """
  List View

  Display all :model:`auth.User` that the user has permission.

  **Templates**

    :template:`key/list.html`.

  **Context**

    tableHead
      Table head with label of: "full_name" and "email".
    regions
      List of :model:`auth.User`.
  """

  friends = Friend.objects.get_blocked_friends(user = request.user)
  
  return render(request, 'friend/list.html',
    {'friends': friends})
