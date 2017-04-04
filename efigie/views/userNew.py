# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from efigie.controllers import *
from efigie.views import *
from efigie.forms import *

@never_cache
@csrf_protect
def userNew(request, alert='', description=''):
  if request.user.is_authenticated():
    return redirect(index)

  form = UserNewForm(request.POST or None)
  
  if form.is_valid():
    user = form.save()
    user = authenticate(username=user.username, password=form.cleaned_data['password1'])
    login(request, user)
    return redirect(index)

  return render(request, '_template_login.html', 
    {'form': form, 
     'button': 'Cadastrar-se',
     'alert': alert,
     'description': description})