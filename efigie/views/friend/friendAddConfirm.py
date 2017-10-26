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
def friendAddConfirm(request, userId):

  user = User.objects.get(id=userId)

  if Friend.objects.filter(user=user, friend=request.user).exists():
    friendship = Friend.objects.get(user=user, friend=request.user)
    friendship.friendship = True
    friendship.save()

    notif = Notification.objects.get(user=request.user,
      notification_type=ContentType.objects.get_for_model(Friend),
      notification_id=friendship.id,
      category=Notification.Category.FRIEND_ADD)

    notif.category=Notification.Category.FRIEND_I_ACCEPT
    notif.save()

    friendship2 = Friend(user=request.user, friend=friendship.user, friendship=True)
    friendship2.save()

    notf2 = Notification(user=friendship2.friend,
      notification=friendship2,
      category=Notification.Category.FRIEND_ACCEPT_YOU)
    notf2.save()

  #AGARD SEND EMAIL

  return redirect(notifications)
