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
@model_required(User, 'friendSearch')
def friendDelete(request, userId):

  user = User.objects.get(id=userId)

  if Friend.objects.filter(user=request.user, friend=user).exists():
    friendship = Friend.objects.get(user=request.user, friend=user)
    friendship.blocked = True
    friendship.friendship = False
    friendship.save()
    notf = Notification.objects.filter(user=user,
      notification_type=ContentType.objects.get_for_model(Friend),
      notification_id=friendship.id)
    notf.delete()
    friendship.delete()

  if Friend.objects.filter(user=user, friend=request.user).exists():
    friendship = Friend.objects.get(user=user, friend=request.user)

    notf = Notification.objects.filter(user=request.user,
      notification_type=ContentType.objects.get_for_model(Friend),
      notification_id=friendship.id)
    notf.delete()
    friendship.delete()

  page = request.META.get('HTTP_REFERER' or None)
  return redirect(page if page != None else friendList)
