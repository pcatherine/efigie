#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from efigie.utils import invariants, Effigy
from efigie.views.decorators import model_required, breadcrumbs

from efigie import *
from efigie.forms import *
from efigie.models import Message
from efigie.views import *
from efigie.views.message import *

@login_required
@breadcrumbs(['index', 'messageWrite'])
@csrf_protect
def messageWrite(request):
  # AGARD ADD GOOGLE
  form = MessageWriteForm(request.POST or None, request.FILES or None, user=request.user)
  if form.is_valid():

    uf = UserEffigy.objects.get(user = request.user)
    image = form.save(uf.settings)

    return render(request, 'message/write_ok.html',
      {'image': image })

  return render(request, 'message/form.html',
    {'form': form,
     'button': 'Encrypt'})
