#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from efigie import *
from efigie.forms import *
from efigie.views import *
from efigie.views.user import *


@csrf_protect
@never_cache
def userLogin(request):
  if request.user.is_authenticated():
    return redirect(index)

  form = UserLoginForm(request.POST or None)
  if form.is_valid():
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']

    user = None
    if '@' in username:
      if User.objects.filter(email=username).exists():
        user = User.objects.get(email=username)
        user = authenticate(username=user.username, password=password)
    else:
      user = authenticate(username=username, password=password)

    if user is not None:
      login(request, user)
      next_url = request.GET.get('next' or None)
      return redirect(next_url if next_url != None else index)
    else:
      messages.error(request, _('Invalid email or password.'))

  return render(request, 'template_login.html',
    {'form': form,
     'button': 'Login',
     'links': [{'name':_('Forgot your password?'), 'url': 'userPasswordReset'},
               {'name':_('Sign Up'), 'url': 'userNew'} ]})
