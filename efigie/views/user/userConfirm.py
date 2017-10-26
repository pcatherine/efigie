#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from efigie.utils import invariants

from efigie import *
from efigie.forms import *
from efigie.models import UserConfirmation
from efigie.views import *
from efigie.views.user import *


@csrf_protect
@never_cache
def userConfirm(request, token):
  if UserConfirmation.objects.filter(token=token, category=UserConfirmation.Category.PASSWORD, confirmed=False).exists():
    reset = get_object_or_404(UserConfirmation, token=token)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
      form.save()
      reset.confirmed = True
      reset.confirmed_by = UserConfirmation.Confirm.USER
      reset.save()
      messages.success(request, invariants.alert_update_success % {
        'model_name': '', 
        'item_name': capfirst(User._meta.get_field('password').verbose_name)})

      return redirect(userLogin)
  elif UserConfirmation.objects.filter(token=token, category=UserConfirmation.Category.VERIFICATION, confirmed=False).exists():
    reset = get_object_or_404(UserConfirmation, token=token)
    reset.confirmed = True
    reset.confirmed_by = UserConfirmation.Confirm.USER
    reset.save()
    login(request, reset.user)
    return redirect(index)
  elif UserConfirmation.objects.filter(token=token, confirmed=True, confirmed_by=UserConfirmation.Confirm.USER).exists():
    messages.info(request, invariants.alert_already_validated % {
      'field_token': UserConfirmation._meta.get_field('token').verbose_name})
    return redirect(userLogin)
  else:
    messages.error(request, invariants.alert_not_found_error % {
      'model_name': UserConfirmation._meta.get_field('token').verbose_name})
    return redirect(userLogin)

  return render(request, 'template_login.html',
    {'form': form,
     'button': invariants.button_edit })
