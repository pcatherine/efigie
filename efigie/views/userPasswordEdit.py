#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from efigie.forms import *
from efigie.views import *

@csrf_protect
@login_required
def userPasswordEdit(request, form=None):
  form = UserPasswordEditForm(user=request.user, data=request.POST or None)
  if form.is_valid():
    form.save()
    messages.success(request, 'Senha editados com sucesso.')
    return redirect(userLogout)

  return render(request, 'form.html',
    {'title': 'Edição de Senha',
     'form': form,
     'button': 'Editar'})