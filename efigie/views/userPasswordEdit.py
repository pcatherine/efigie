# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from efigie.controllers import *
from efigie.views import *
from efigie.forms import *

@login_required
def userPasswordEdit(request, form=None):
  form = UserPasswordEditForm(user=request.user, data=request.POST or None)
  if form.is_valid():
    form.save()
    messages.success(request, 'Senha editados com sucesso.')
    return redirect(userLogout)

  return render(request, 'a_user_edit.html',
    {'form': form,
     'button': 'Editar'})