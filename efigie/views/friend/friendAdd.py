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
def friendAdd(request, userId):

  user = User.objects.get(id=userId)

  if Friend.objects.relationship(user=request.user, friend=user) == None:
    friendship = Friend(user=request.user, friend=user)
    friendship.save()

    notif = Notification(user=user, notification=friendship, category=Notification.Category.FRIEND_ADD)
    notif.save()

      #AGARD SEND EMAIL
  if request.is_ajax():
    return JsonResponse({}, status = 200, safe=False)

  page = request.META.get('HTTP_REFERER' or None)
  return redirect(page if page != None else friendSearch)
