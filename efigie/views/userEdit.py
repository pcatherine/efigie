#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from efigie.views import *
from efigie.forms import *

@csrf_protect
@login_required
def userEdit(request):
  form = UserEditForm(user=request.user, data=request.POST or None)
  if form.is_valid():
    form.save(request.build_absolute_uri(None))
    messages.success(request, 'Dados editados com sucesso.')
    return redirect(userSettings)

  return render(request, 'form.html',
    {'title': 'Edição de Dados',
     'form': form,
     'button': 'Editar'})