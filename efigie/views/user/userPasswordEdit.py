#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect

from efigie.views import *
from efigie.views.user import *

@login_required
@csrf_protect
@breadcrumbs(['index', 'userSettings' ,'userPasswordEdit'])
def userPasswordEdit(request, form=None):

  form = PasswordChangeForm(user=request.user, data=request.POST or None)
  if form.is_valid():
    form.save()
    messages.success(request, invariants.alert_update_success % {
      'model_name': capfirst(User._meta.get_field('password').verbose_name),
      'item_name':''})
    return redirect(userLogout)

  return render(request, 'user/form.html',
    {'form': form,
     'button': invariants.button_edit })
