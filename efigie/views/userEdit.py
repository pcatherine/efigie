# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from efigie.views import *

from efigie.forms import *

@login_required
def userEdit(request):
  form = UserEditForm(user=request.user, data=request.POST or None)
  if form.is_valid():
    form.save(request.build_absolute_uri(None))
    return redirect(userSettings)

  return render(request, 'user_edit.html',
    {'form': form,
     'button': 'Editar'})