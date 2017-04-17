# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from efigie.controllers import EffigyCommunication
from efigie.forms import *
from efigie.views import *


@login_required
def userSettings(request, alert='', description=''):
  form = UserLoginForm(request.POST or None)

  if form.is_valid():
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']

    if (username == request.user.username) or (username == request.user.email):
      if request.user.check_password(password):
        return redirect(userLogout)





  return render(request, 'user_settings.html',
    {'form': form})