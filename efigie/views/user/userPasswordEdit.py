#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.csrf import csrf_protect

from efigie.views import *

@login_required
@csrf_protect
@breadcrumbs(['index', 'userSettings' ,'userPasswordEdit'])
def userPasswordEdit(request, form=None):

  form = PasswordChangeForm(user=request.user, data=request.POST or None)
  if form.is_valid():
    form.save()
    messages.success(request, 'Senha editados com sucesso.')
    return redirect(userLogout)

  return render(request, 'user/form.html',
    {'form': form,
     'button': 'Editar'})