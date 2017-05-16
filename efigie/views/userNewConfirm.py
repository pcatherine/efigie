#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth import login
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.cache import never_cache

from efigie import *
from efigie.models import UserConfirmation, Category
from efigie.views import *

@never_cache
def userNewConfirm(request, key):
  if UserConfirmation.objects.filter(key=key, category=Category.VERIFICATION, confirmed=False).exists():
    reset = get_object_or_404(UserConfirmation, key=key)
    reset.confirmed = True
    reset.save()
    login(request, reset.user)
    return redirect(index)
  else:
    raise Http404("Chave não encontrada ou já utilizada")
