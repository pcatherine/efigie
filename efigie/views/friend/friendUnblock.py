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
def friendUnblock(request, userId):

  user = User.objects.get(id=userId)

  if Friend.objects.filter(user=request.user, friend=user).exists():
    friendship = Friend.objects.get(user=request.user, friend=user)
    friendship.delete()

  page = request.META.get('HTTP_REFERER' or None)
  return redirect(page if page != None else friendSearch)
