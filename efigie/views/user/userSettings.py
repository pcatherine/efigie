#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from efigie import *
from efigie.forms import *
from efigie.utils import invariants
from efigie.views import *
from efigie.views.user import *

@login_required
@csrf_protect
@breadcrumbs(['index', 'userSettings'])
def userSettings(request):

  form = UserLoginForm(request.POST or None)

  if form.is_valid():
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']

    if (username == request.user.username) or (username == request.user.email):
      if request.user.check_password(password):
        name = request.user.get_full_name()
        #AGARD verificar se funciona
        request.user.delete()
        messages.success(request, invariants.alert_delete_success % {
          'model_name': capfirst(User._meta.verbose_name),
          'item_name': name})
        return redirect(userLogout)
      else:
        messages.error(invariants.alert_delete_error % {
          'model_name': capfirst(User._meta.verbose_name),
          'item_name': request.user.get_full_name()})

  return render(request, 'user/settings.html',
    {'form': form})
