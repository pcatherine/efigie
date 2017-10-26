#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect

from efigie import *
from efigie.forms import *
from efigie.utils import invariants
from efigie.views import *
from efigie.views.user import *


@csrf_protect
def userPasswordReset(request):
  form = UserPasswordResetForm(request.POST or None)

  if form.is_valid():
    form.save(request.build_absolute_uri(None))
    messages.success(request, invariants.mail_success % {
      'field_email': capfirst(User._meta.get_field('email').verbose_name)})
    return redirect(userLogin)

  return render(request, 'template_login.html',
    {'form': form,
     'button': _('Send me the instructions') })
