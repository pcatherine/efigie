# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from efigie.controllers import EffigyCommunication
from efigie.forms import *
from efigie.views import *


@never_cache
@csrf_protect
@login_required
def userSettings(request):
  form = UserLoginForm(request.POST or None)

  if form.is_valid():
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']

    if (username == request.user.username) or (username == request.user.email):
      if request.user.check_password(password):
        # request.user.delete()
        messages.success(request, 'Usuario deletado com sucesso.')
        return redirect(userLogout)
      else:
        messages.error(request, 'Usuario nao pode ser excluido.')

  return render(request, 'user_settings.html',
    {'form': form})