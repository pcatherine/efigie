# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from efigie.controllers import *
from efigie.views import *
from efigie.forms import *

def userPasswordReset(request, alert='', description=''):
  form = UserPasswordResetForm(request.POST or None)

  if form.is_valid(): 
    form.save(request.build_absolute_uri(None))
    return redirect(userLogin) 

  return render(request, '_template_login.html', 
    {'form': form,
     'button': 'Restar Senha',
     'alert': alert,
     'description': description})