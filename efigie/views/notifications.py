#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from efigie.views.decorators import breadcrumbs

from efigie.models import Notification
from efigie.views import *


@login_required
@breadcrumbs(['index', 'notifications'])
def notifications(request):
  Notification.objects.filter(user=request.user, read=False).exclude(category=Notification.Category.FRIEND_ADD).update(read=True)

  return render(request, 'notification_timeline.html')
