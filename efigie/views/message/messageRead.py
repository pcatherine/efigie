#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from efigie.forms import *
from efigie.utils import invariants
from efigie.views import *
from efigie.views.message import *


@login_required
@breadcrumbs(['index', 'messageRead'])
@csrf_protect
def messageRead(request):

  form = MessageReadForm(request.POST or None, request.FILES or None, user = request.user)
  try:
    if form.is_valid():
      idMessage, m, s = form.save()
      msg = Message.objects.get(id=int(idMessage))
      if msg.count == -1 or msg.count >= 1:
        if msg.count != -1:
          msg.count -= 1
          msg.save()
        messages.success(request, "%s" % (m))
        form = MessageReadForm(None, user = request.user)
      else:
        messages.error(request, _("This message cannot be read."))
  except ValidationError as e:
    messages.error(request, "".join(e))
  except ValueError as e:
    messages.error(request, e)
  except:
    messages.error(request, invariants.alert_not_found_error % {
      'model_name': Message._meta.verbose_name.title()})

  return render(request, 'message/form.html',
    {'form': form,
     'button': _('Decrypt')})
