# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from efigie import *
from efigie.controllers import *
from efigie.forms import *
from efigie.models import Category
from efigie.views import *

@never_cache
def userNewConfirm(request, alert='', description=''):
  if UserVerification.objects.filter(key=key, category=Category.VERIFICATION, confirmed=False).exists():
    reset = get_object_or_404(UserVerification, key=key)
    reset.confirmed = True
    reset.save()
    login(request, user)
    return redirect(index)
  else:
    return redirect(userNew)
