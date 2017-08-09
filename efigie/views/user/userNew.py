#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from efigie import *
from efigie.forms import *
from efigie.views import *

@csrf_protect
@never_cache
def userNew(request):
  if request.user.is_authenticated():
    return redirect(index)

  form = UserNewForm(request.POST or None)

  if form.is_valid():
    user = form.save(request.build_absolute_uri(None))
    user = authenticate(username=user.username, password=form.cleaned_data['password1'])
    login(request, user)
    return redirect(index)

  return render(request, 'template_login.html',
    {'form': form,
     'button': 'Cadastrar-se'})
