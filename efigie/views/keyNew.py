# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from efigie import *
from efigie.controllers import *
from efigie.forms import *
from efigie.models import Category
from efigie.views import *

@csrf_protect
@login_required
def keyNew(request):
  form = KeyForm(user=request.user, data=request.POST or None)
  
  if form.is_valid():
    form.save()
    messages.success(request, 'Chave criada com sucesso.')
    return redirect(userSettings)

  return render(request, 'form.html',
    {'title': 'Nova Chave',
     'form': form,
     'button': 'Criar Chave'})