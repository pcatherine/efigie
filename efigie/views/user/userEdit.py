#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.text import capfirst

from efigie.utils import invariants
from efigie.views.decorators import model_required, breadcrumbs

from efigie.forms import *
from efigie.views import *
from efigie.views.user import *


@login_required
@breadcrumbs(['index', 'userSettings', 'userEdit'])
@csrf_protect
def userEdit(request):

  form = UserEditForm(user=request.user, data=request.POST or None)
  if form.is_valid():
    form.save(request.build_absolute_uri(None))
    messages.success(request, invariants.alert_update_success % (capfirst(User._meta.verbose_name)))
    return redirect(userSettings)

  return render(request, 'form.html',
    {'form': form,
     'button': invariants.button_edit % (capfirst(User._meta.verbose_name)) })
