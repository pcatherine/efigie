# !/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from efigie import *
from efigie.forms import *
from efigie.models import Key
from efigie.views import *
from efigie.views.key import *

@login_required
@breadcrumbs(['index', 'keyList', 'keyImport'])
@csrf_protect
def keyImport(request):
  form = KeyImportForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    file = request.FILES['file']
    try:
      date = file.read().decode('utf-8')
      privateKey, publicKey, name, size = date.split(';')

      valid, name = form.save(user=request.user, privateKey=privateKey, publicKey=publicKey, name=name, size=size)

      if valid:
        messages.success(request, 'Chave <b>%s</b> importada com sucesso.' % (name))
        return redirect(keyList)
      else:
        messages.info(request, 'Chave <b>%s</b> já importada.' % (name))
        return redirect(keyImport)

    except Exception as e:
      messages.error(request, 'O arquivo não pode ser importado.')
      return redirect(keyImport)


  return render(request, 'form.html',
    {'title': 'Importação de Chave',
     'form': form,
     'button': 'Importar'})
