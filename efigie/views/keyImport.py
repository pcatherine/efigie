    #!/usr/bin/python
#-*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from efigie.views import *
from efigie.forms import *

@csrf_protect
@login_required
def keyImport(request):
  form = KeyImportForm(request.POST or None)
  
  if form.is_valid():
    return redirect(keyList)

  return render(request, 'form.html',
    {'title': 'Importação de Chave',
     'form': form,
     'button': 'Importar'})