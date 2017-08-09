#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from efigie import *
from efigie.forms import *
from efigie.views import *

@csrf_protect
def userPasswordReset(request):
  form = UserPasswordResetForm(request.POST or None)

  if form.is_valid(): 
    form.save(request.build_absolute_uri(None))
    return redirect(userLogin) 

  return render(request, 'template_login.html', 
    {'form': form,
     'button': 'Restar Senha'})