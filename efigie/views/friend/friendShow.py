#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect

from efigie.views.decorators import model_required, breadcrumbs

from efigie import *
from efigie.models import Friend, Notification
from efigie.views import *
from efigie.views.friend import *

@login_required
@model_required(User, 'friendSearch')
@breadcrumbs(['index', 'friendList', ('friendShow', 'userId') ])
def friendShow(request, userId):

  user = User.objects.get(id=userId)

  if user == request.user:
    return redirect(userSettings)

  if Friend.objects.filter(user=user, friend=request.user, blocked=True):
    return redirect(friendSearch)


  if Friend.objects.filter(user=request.user, friend=user).exists():
    f = Friend.objects.get(user=request.user, friend=user)

    if not f.friendship and not f.blocked:
      category = 2
    elif not f.friendship and f.blocked:
      category = 4
    elif f.friendship and not f.blocked:
      category = 3
    elif f.friendship and f.blocked:
      category = 4
  elif Friend.objects.filter(user=user, friend=request.user).exists():
    category = 2
  else:
    category = 1

  return render(request, 'friend/show.html',
    {'friend': user,
     'category': category})
