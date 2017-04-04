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
def userLogin(request, alert='', description=''):
  if request.user.is_authenticated():
    return redirect(index)

  form = UserLoginForm(request.POST or None)
  if form.is_valid():
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']

    if '@' in username:
      try:
        user = User.objects.get(email=username)
        user = authenticate(username=user.username, password=password)
      except Exception as e:
        alert = 'danger'
        description = 'Username ou senha inválido.'
    else:
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect(index)
      else: 
        alert = 'danger'
        description = 'Username ou senha inválido.'

  return render(request, 'user_login.html', 
    {'form': form, 
     'alert': alert,
     'description': description})