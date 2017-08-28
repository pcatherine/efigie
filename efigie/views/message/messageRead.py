#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from efigie.forms import *
from efigie.utils import invariants
from efigie.views import *

@login_required
@breadcrumbs(['index', 'messageRead'])
@csrf_protect
def messageRead(request):

  try:
    form = MessageReadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
      idMessage, m, s = form.save()
      msg = Message.objects.get(id=int(idMessage))
      if msg.count == -1 or msg.count >= 1:
        if msg.count != -1:
          msg.count -= 1
          msg.save()
        messages.success(request, "%s" % (m))
        form = MessageReadForm(None)

      else:
        messages.error(request, "This message cannot be read.")
  except ValidationError as e:
    messages.error(request, "".join(e))
  except ValueError as e:
    messages.error(request, e)
  except:
    messages.error(request, invariants.alert_not_found_error % (Message._meta.verbose_name.title()))

  return render(request, 'message/form.html',
    {'form': form,
     'button': 'Decrypt'})
