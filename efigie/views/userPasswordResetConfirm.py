#!/usr/bin/python
#-*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from efigie import *
from efigie.forms import *
from efigie.models import UserConfirmation, Category
from efigie.views import *

@csrf_protect
@never_cache
def userPasswordResetConfirm(request, key):
  if UserConfirmation.objects.filter(key=key, category=Category.PASSWORD, confirmed=False).exists():
    reset = get_object_or_404(UserConfirmation, key=key)
    form = UserSetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
      form.save()
      reset.confirmed = True
      reset.save()
      return redirect(userLogin)
  else:
    raise Http404("Chave não encontrada ou já utilizada")

  return render(request, 'template_login.html', 
    {'form': form, 
     'button': 'Alterar Senha'})
