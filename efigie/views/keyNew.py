#!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from efigie import *
from efigie.forms import *
from efigie.views import *

@csrf_protect
@login_required
def keyNew(request):
  form = KeyForm(user=request.user, data=request.POST or None)
  
  if form.is_valid():
    form.save()
    messages.success(request, 'Chave <b>%s</b> criada com sucesso.' % (form.cleaned_data['identifier']))
    return redirect(keyList)

  return render(request, 'form.html',
    {'title': 'Criação de Chave RSA',
     'form': form,
     'button': 'Criar Chave'})