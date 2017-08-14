#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.utils.text import capfirst


from efigie.utils import invariants
from efigie.views.decorators import model_required, breadcrumbs

from efigie import *
from efigie.forms import *
from efigie.models import UserConfirmation, Category
from efigie.views import *

@csrf_protect
@never_cache
def userConfirm(request, token):
  if UserConfirmation.objects.filter(token=token, category=Category.PASSWORD, confirmed=False).exists():
    reset = get_object_or_404(UserConfirmation, token=token)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
      form.save()
      reset.confirmed = True
      reset.save()
      return redirect(userLogin)
  elif UserConfirmation.objects.filter(token=token, category=Category.VERIFICATION, confirmed=False).exists():
    reset = get_object_or_404(UserConfirmation, token=token)
    reset.confirmed = True
    reset.save()
    login(request, reset.user)
    return redirect(index)
  else:
    raise Http404(invariants.alert_not_found % ("Token"))

  return render(request, 'template_login.html',
    {'form': form,
     'button': invariants.button_edit % capfirst(User._meta.get_field('password').verbose_name)})
